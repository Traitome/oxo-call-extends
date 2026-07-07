---
name: truvari
category: analysis
description: Truvari - Structural variant benchmarking, merging, and annotation for VCF files (bench, collapse, phab, anno, etc.).
tags: [truvari, vcf-comparison, variant-analysis, structural-variants, sv, bioinformatics, genomics, benchmarking]
author: oxo-call-community
source_url: "https://github.com/ACEnglish/truvari"
---

## Concepts

- **Tool Overview**: Truvari is a Python package for structural-variant (SV) benchmarking, merging, and annotation in VCF/BCF files. It computes recall/precision/F1 between a baseline truth set and a comparison set of calls, collapses redundant variants, harmonises representations via MSA, and annotates VCFs with population/repeat/mappability signals.
- **Top-level Commands** (Truvari v5.x):
  - **Benchmarking**: `bench`, `refine`
  - **Merging**: `collapse`, `phab`
  - **Analysis**: `consistency`, `stratify`, `vcf2df`, `stratp`
  - **Annotation**: `anno` (with subcommands `addid`, `bpovl`, `chunks`, `density`, `dpcnt`, `gcpct`, `grm`, `grpaf`, `gtcnt`, `hompct`, `lcr`, `numneigh`, `remap`, `repmask`, `svinfo`, `trf`)
  - **Misc**: `segment`, `divide`, `ga4gh`, `version`
- **`bench` Matching Algorithm**: For each pair of variants, Truvari compares five dimensions:
  | Parameter | Default | Definition |
  |---|---|---|
  | `--refdist` (`-r`) | 500 | Max reference-distance between base and comp breakpoints |
  | `--pctseq` (`-p`) | 0.7 | Min edit-distance similarity of REF/ALT haplotype sequences |
  | `--pctsize` (`-P`) | 0.7 | Min ratio of min(size)/max(size) between the two variants |
  | `--pctovl` (`-O`) | 0.0 | Min reciprocal overlap (overlapping bp / longest span) |
  | `--typeignore` (`-t`) | False | If set, types need not match (e.g. DEL vs INV allowed) |
- **`bench` Output Directory** (always written to `-o`):
  - `tp-base.vcf.gz` / `tp-comp.vcf.gz` — true positives from each side
  - `fp.vcf.gz` — false positives (in comp, not in base)
  - `fn.vcf.gz` — false negatives (in base, not in comp)
  - `summary.json` — recall/precision/F1, TP-base, TP-comp, FP, FN, base cnt, comp cnt, gt_concordance, gt_matrix, weighted metrics
  - `params.json` — exact parameters used (for reproducibility)
  - `candidate.refine.bed` — regions for `refine`/`phab` follow-up
  - `log.txt` — run log
- **Per-call Annotations** added to output VCFs: `TruScore` (= `(pctseq+pctsize+pctovl)/3 * 100`), `PctSeqSimilarity`, `PctSizeSimilarity`, `PctOvlSimilarity`, `MatchId`, `MatchDiff`, `SVTYPE`, `SVLEN`, `PctIdt`.
- **`collapse`** merges redundant SVs in a single call set; `--keep {first,maxqual,common}` chooses which survivor to keep. Useful for merging caller outputs before benchmarking.
- **`phab`** uses Multiple Sequence Alignment (MAFFT/WFA/POA) to harmonise different but equivalent variant representations before re-benching; `refine` automates `phab`+`bench` on `bench` outputs.
- **`anno` Subcommands**: Each adds a different INFO/FORMAT annotation. Notable ones:
  - `grpaf` — allele frequencies per sample group (`-l labels.tsv`, tags: AF, MAF, ExcHet, HWE, MAC, AC, AN).
  - `trf` — tandem-repeat motif & copy-number annotations (requires `trf409.linux64`).
  - `remask` — repeat-masker overlap; `lcr` — low-complexity regions; `grm` — mappability.
- **Installation**: `pip install truvari` (Python ≥3.7) or `conda install -c bioconda truvari`. Requires `pysam`, `pyvcf3`. Some `anno` subcommands need external binaries (`mafft`, `trf409.linux64`).
- **Use Case**: SV caller benchmarking against truth sets (e.g. GIAB); merging multi-caller SV VCFs; annotating SVs with population AF or repeat context; structural-variant QC.

## Pitfalls

- **Symbolic SVs require a reference**. `bench -f ref.fa` is mandatory when VCFs contain `<DEL>`, `<INS>`, `<DUP>`, `<INV>`, or BND records; without it, sequence-based metrics cannot be computed and matches are unreliable. Pass `-w`/`--write-resolved` to materialise symbolic alleles into their resolved sequence.
- **Defaults (refdist 500, pctseq 0.7, pctsize 0.7) are strict**. Coverage-based callers (CNVnator, ERDS) report fuzzy boundaries and may be penalised unfairly; relax to `-p 0 -P 0.5 -O 0.5 -r 1000` for those. Start strict, then relax incrementally while inspecting `summary.json`.
- **`--sizemin 50` (base) and `--sizefilt 30` (comp) differ on purpose**. The base threshold is higher to mirror truth-set conventions; if your truth set includes sub-50bp variants, lower both or you'll get artificial FN counts.
- **`--sizemax 50000` silently truncates large SVs**. Set `--sizemax -1` to disable the cap when benchmarking very large CNVs or chromosomal-scale events.
- **Variant representation must be consistent**. Left-normalise, single-allele-per-line, decompose multi-allelics (`bcftools norm -m -any`) before `bench`. Different representations of the same haplotype (e.g. one DEL vs two adjacent DELs) will be reported as FP+FN; use `phab`/`refine` to harmonise.
- **`--pick single` (default) assigns one-to-one matches**. For multi-mapping scenarios (e.g. a caller splits one truth SV into two), `--pick ac` (allele-count) or `--pick multi` gives more credit but inflates recall. Document which one was used for reproducibility.
- **`--passonly` filters on `FILTER==PASS`**. If your comparison VCF has `LowQual`/`MinDP` filters you want to include, omit `--passonly` or pre-filter the VCF explicitly.
- **BND matching uses `--bnddist 100`** (default). Lower it for tighter breakpoint requirements; set `-B -1` to disable BND distance checking (BNDs matched only by sequence similarity).
- **`collapse --chain` can transitively merge unrelated SVs**. Chaining extends matches through intermediate calls; useful for redundant caller ensembles but may merge adjacent real events. Verify with `--removed-output removed.vcf`.
- **`anno grpaf` needs a labels file**. The `--labels` TSV has two columns `sample<TAB>group`; a missing sample silently drops it unless `--strict` is set. Always run `truvari anno grpaf --strict` to catch typos.
- **`anno trf` needs the `trf409.linux64` binary**. Pass `-e /path/to/trf409.linux64` or it won't run. The reference repeat annotations (`-r`) are also required; obtain them from the Truvari repo or build with `truvari segment` + RepeatMasker.
- **`refine` only helps when `phab` can harmonise representations**. If base/comp VCFs use fundamentally different reference assemblies, `refine` will not fix the mismatch; run liftover first.

## Examples

### Basic SV benchmarking against a truth set
**Args:** `truvari bench -b truth_sv.vcf.gz -c caller_sv.vcf.gz -f hg38.fa -o bench_out/`
**Explanation:** `-b` is the baseline truth set, `-c` is the comparison caller output, `-f hg38.fa` is needed because symbolic SVs (`<DEL>` etc.) require sequence resolution. The directory `bench_out/` will contain `tp-base.vcf.gz`, `tp-comp.vcf.gz`, `fp.vcf.gz`, `fn.vcf.gz`, `summary.json`, `params.json`, and `log.txt`.

### Benchmark with relaxed thresholds for fuzzy callers
**Args:** `truvari bench -b base.vcf.gz -c comp.vcf.gz -f ref.fa -o bench_loose/ -r 1000 -p 0 -P 0.5 -O 0.5`
**Explanation:** `-r 1000` allows up to 1 kb breakpoint shift; `-p 0` disables sequence similarity (useful for CNVnator-like fuzzy calls); `-P 0.5` and `-O 0.5` require only 50% size/overlap match. Suitable for coverage-based SV callers; results will be more permissive than the strict defaults.

### Benchmark only PASS calls within target regions
**Args:** `truvari bench -b base.vcf.gz -c comp.vcf.gz -f ref.fa -o bench_targeted/ --passonly --includebed regions.bed`
**Explanation:** `--passonly` ignores any non-PASS call in either VCF; `--includebed regions.bed` only counts variants overlapping the target intervals; `--extend 0` (default) does not allow calls to bleed outside the BED.

### Merge and benchmark multiple callers
**Args:** `truvari collapse -i merged_raw.vcf.gz -o collapsed.vcf.gz --keep maxqual -c removed.vcf -f ref.fa && truvari bench -b truth.vcf.gz -c collapsed.vcf.gz -f ref.fa -o bench/`
**Explanation:** `collapse --keep maxqual` retains the highest-quality call among redundant SVs and writes the discarded ones to `removed.vcf`; then `bench` evaluates the consensus against truth. This is the canonical multi-caller ensemble workflow.

### Collapse redundant SVs with chaining
**Args:** `truvari collapse -i calls.vcf.gz -o collapsed.vcf.gz --chain --keep common -f ref.fa --median-info`
**Explanation:** `--chain` allows transitive collapsing (A~B and B~C → A~C merged); `--keep common` keeps the variant in the most samples for multi-sample VCFs; `--median-info` stores median start/end/size of all collapsed entries in the survivor's INFO.

### Run bench with automatic refinement
**Args:** `truvari bench -b base.vcf.gz -c comp.vcf.gz -f ref.fa -o bench/ --refine`
**Explanation:** `--refine` automatically runs `truvari refine` on the result, which uses `phab` (MSA-based harmonisation) to re-evaluate FN/FP pairs that differ only in representation. Produces `bench/refine.base.vcf.gz`, `bench/refine.comp.vcf.gz`, `bench/refine.variant_summary.json`, and `bench/phab_bench/`.

### Genotype-aware benchmarking
**Args:** `truvari bench -b base.vcf.gz -c comp.vcf.gz -f ref.fa -o bench/ --bSample NA12878 --cSample NA12878`
**Explanation:** `--bSample` and `--cSample` force specific samples (must exist in both VCFs). `summary.json` will report `TP-comp_TP-gt`, `TP-comp_FP-gt`, and `gt_concordance` = TP-comp_TP-gt / (TP-comp_TP-gt + TP-comp_FP-gt), allowing you to score genotype accuracy beyond mere presence.

### Restrict to a size range and disable type matching
**Args:** `truvari bench -b base.vcf.gz -c comp.vcf.gz -f ref.fa -o bench/ -s 50 -S 30 --sizemax 100000 -t`
**Explanation:** `-s 50` / `-S 30` set minimum variant sizes from base/comp; `--sizemax 100000` caps at 100 kb; `-t`/`--typeignore` allows e.g. a DEL in base to match an INV in comp, useful when caller SVTYPE assignments are inconsistent.

### Annotate SVs with per-group allele frequencies
**Args:** `truvari anno grpaf -i calls.vcf.gz -o calls.grpaf.vcf.gz -l sample_groups.tsv --strict`
**Explanation:** `grpaf` adds `AF_<group>`, `MAF_<group>`, `ExcHet_<group>`, `HWE_<group>`, `MAC_<group>`, `AC_<group>`, `AN_<group>` per group defined in `sample_groups.tsv` (columns: `sample<TAB>group`). `--strict` exits if a sample is missing from the VCF.

### Annotate SVs with tandem-repeat context
**Args:** `truvari anno trf -i calls.vcf.gz -o calls.trf.vcf.gz -f hg38.fa -r repeats.bed -e /usr/local/bin/trf409.linux64`
**Explanation:** `trf` annotates each SV with the best-fitting tandem-repeat motif (`TRF` field), copy number, and motif similarity; `-r repeats.bed` is the reference repeat annotation; `-e` points to the Tandem Repeats Finder binary. Useful for distinguishing true SVs from reference repeat polymorphisms.

### Convert VCF to a pandas DataFrame for analysis
**Args:** `truvari vcf2df calls.vcf.gz calls.pkl --info SVTYPE SVLEN TruScore --format GT GQ`
**Explanation:** `vcf2df` writes a pickled pandas DataFrame; `--info` selects INFO fields, `--format` selects FORMAT fields. Enables downstream `pandas`/`seaborn` analysis without manual VCF parsing.

### Get variant counts stratified by BED regions
**Args:** `truvari stratify calls.vcf.gz regions.bed > strat.tsv`
**Explanation:** `stratify` counts how many variants in `calls.vcf.gz` overlap each BED region, writing a TSV with region coordinates and per-region variant counts. Useful for comparing caller density across chromosome arms or difficult regions.

### Segment SVs into disjoint genomic regions
**Args:** `truvari segment -i calls.vcf.gz -o segments.bed -f ref.fa`
**Explanation:** `segment` normalises SVs into non-overlapping genomic intervals and writes a BED of disjoint regions, useful as input for `--includebed` or for computing SV density across the genome.

### Print Truvari version
**Args:** `truvari version`
**Explanation:** Prints the installed Truvari version (e.g. `Truvari v5.4.0`). Always include in benchmarking reports for reproducibility.
