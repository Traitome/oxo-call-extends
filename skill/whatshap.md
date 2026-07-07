---
name: whatshap
category: bioinformatics
description: WhatsHap - Read-based haplotype phasing of variants from sequencing reads (Illumina/PacBio/Nanopore), with pedigree and polyploid modes.
tags: [whatshap, haplotype-phasing, bioinformatics, genomics, long-read, phasing]
author: oxo-call-community
source_url: "https://github.com/whatshap/whatshap"
---

## Concepts

- **Tool Overview**: WhatsHap is a read-based phasing tool: it reconstructs the two haplotypes of a diploid individual from a VCF of variants plus a BAM/CRAM of sequencing reads covering those variants. Especially powerful for long reads (PacBio HiFi, ONT) but also works for Illumina.
- **Subcommands**:
  - `phase` — diploid read-based phasing (core algorithm: `whatshap`, `hapchat`, or `heuristic`).
  - `polyphase` / `polyphasegenetic` — polyploid phasing (auto/polyploid, optionally with progeny).
  - `haplotag` — tag reads in a BAM with `HP`/`PS` tags using an already-phased VCF.
  - `haplotagphase` — phase a VCF using a haplotagged BAM.
  - `stats` — print phasing statistics (block count, NG50, etc.).
  - `compare` — compare two or more phased VCFs.
  - `genotype`, `find_snv_candidates`, `learn`, `split`, `unphase`, `hapcut2vcf` — auxiliary utilities.
- **Phasing Algorithm**: WhatsHap computes a minimum error-correction (MEC) solution via dynamic programming over the read–variant bipartite graph. `--algorithm` selects among `whatshap` (default, exact for moderate coverage), `hapchat` (alternative exact solver), or `heuristic` (for very high coverage; controlled by `--row-limit`).
- **Variant Support**: With `--reference`, WhatsHap can phase SNVs, insertions, deletions, MNPs, and complex substitutions (e.g. `TGCA → AAC`). Without a reference (`--no-reference`), only SNVs, insertions, and deletions are phased. **Structural variants are never phased.**
- **VCF Representation**: Output uses the standardized `GT:PS` (phase set) notation by default; `--tag HP` switches to the `HP` tag style used by GATK ReadBackedPhasing. Each phased block shares a `PS` integer; `|` separators in `GT` indicate phased alleles (e.g. `0|1`).
- **Pedigree Phasing** (`--ped PED/FAM`): Uses reads from related individuals (e.g. mother–father–child trio) to improve phasing and reduce required coverage. Optionally combined with `--genmap FILE` (genetic map for recombination modelling) and `--recombrate C` (constant recombination rate in cM/Mb).
- **Multi-Sample / Multi-BAM**: A multi-sample VCF is phased per-sample; pass one BAM per sample and match via `@RG`/`SM`. `--ignore-read-groups` forces all reads to one sample. Multiple BAMs from different technologies can be combined in one invocation.
- **Recommended Workflow** (per official docs): Call variants from high-quality short reads (Illumina), then phase with long reads (PacBio HiFi / ONT) using `--reference` for re-alignment allele detection.
- **Input Requirements**:
  - VCF: gzip or plain; for `haplotag` it **must** be bgzipped and indexed (`.tbi`/`.csi`).
  - BAM/CRAM: coordinate-sorted and indexed (`.bai`/`.csi`); CRAM needs `--reference`.
  - Reference: FASTA + `.fai` (create with `samtools faidx`).
- **Installation**: `conda install -c bioconda whatshap` or `pip install whatshap`.
- **Use Case**: Haplotype assembly; resolving compound heterozygous variants; phasing for expression/QTL analysis; read-backed phasing of clinical variants.

## Pitfalls

- **`haplotag` requires a bgzipped + indexed VCF**. Plain `gzip` will not work — use `bgzip` (from htslib) and `tabix -p vcf phased.vcf.gz`. WhatsHap will refuse to start otherwise.
- **Structural variants are silently skipped**. WhatsHap phases SNVs, indels, MNPs and complex substitutions but never BND/DEL/INV/DUP symbolic SVs; if you need SV phasing use a different tool (e.g. WhatsHap's `haplotag` with SV VCFs is unsupported — read coverage alone is too coarse for breakpoints).
- **`--no-reference` degrades long-read phasing quality**. Without a reference, WhatsHap cannot re-align reads to candidate alleles, so error-prone long reads (PacBio CLR, ONT R9/10) mis-call alleles around indels. Always supply `--reference` for long reads when possible.
- **Default `--mapping-quality 20` may exclude valid long reads**. PacBio/ONT alignments often have MAPQ below 20 in repetitive regions; consider lowering to `--mapping-quality 10` for long reads, but verify specificity on a small test set first.
- **`--internal-downsampling 15` quietly caps coverage**. The default 15× cap means very deep data is downsampled internally; raising it improves phasing marginally but runtime grows **exponentially**. Avoid changing it unless directed by the docs.
- **PED file column order matters**. PED/FAM files have fixed columns `family_id individual_id father_id mother_id sex phenotype`; the `--ped` parser expects the child, father, and mother to all be present in the VCF sample names. A swapped parent column silently produces wrong phasing.
- **`HP` vs `PS` tag is not interchangeable across downstream tools**. GATK and some legacy tools expect `HP:i:1`/`HP:i:2`, while modern VCFs standardize on `PS`. Use `--tag HP` only when feeding GATK ReadBackedPhasing-compatible pipelines.
- **`whatshap haplotag` does not phase**. It only adds `HP`/`PS` tags to reads based on an **already-phased** VCF. If you need phasing, run `whatshap phase` first, then `haplotag` if you want tagged reads.
- **Supplementary alignments need explicit handling**. By default `haplotag` tags only the primary alignment. Use `--tag-supplementary copy-primary` (tag like primary), `independent-or-skip` (treat as separate; skip if undetermined), or `independent-or-copy-primary` (try independent, fall back to primary). Chosen strategy affects downstream long-read analysis.
- **`stats` requires phased VCF**. Running `stats` on an unphased VCF reports zero blocks and misleading NG50. Run `phase` first or use `--only-snvs` to scope to SNVs only.
- **Multi-sample BAM read groups must be set**. Without `@RG SM:` headers WhatsHap cannot match reads to samples; `--ignore-read-groups` is a fallback for single-sample BAMs only.
- **Pedigree phasing switches the algorithm**. `--ped` mode is no longer pure read-based phasing — it uses Mendelian transmission + recombination inference, so coverage requirements drop but recombinations may be inferred even without supporting reads in parents.

## Examples

### Basic diploid phasing with reference
**Args:** `whatshap phase -o phased.vcf --reference hg38.fa input.vcf aln.bam`
**Explanation:** `phase` runs the default `whatshap` exact algorithm; `--reference hg38.fa` (must have `hg38.fa.fai`) enables re-alignment allele detection for indels/complex variants; output VCF uses `PS` tags by default. Reads below MAPQ 20 are filtered.

### Phase with multiple BAM files (multi-technology)
**Args:** `whatshap phase -o phased.vcf -r ref.fa calls.vcf illumina.bam pacbio.bam`
**Explanation:** Multiple `PHASEINPUT` files are accepted in order; WhatsHap uses `@RG SM:` to attribute reads to samples. Mixing Illumina (high-quality calls) and PacBio (long phasing reads) is the recommended workflow per the official guide.

### Phase only SNVs to speed up long-read input
**Args:** `whatshap phase --only-snvs --mapping-quality 10 -r ref.fa -o phased_snv.vcf calls.vcf ont.bam`
**Explanation:** `--only-snvs` skips indel/complex re-alignment, speeding up very long ONT reads; `--mapping-quality 10` admits lower-MAPQ ONT alignments.

### Use the heuristic algorithm for very high coverage
**Args:** `whatshap phase --algorithm heuristic --row-limit 100 -r ref.fa -o phased.vcf calls.vcf pacbio.bam`
**Explanation:** `--algorithm heuristic` switches from exact MEC to a heuristic suited to deep coverage; `--row-limit 100` controls the memory/time/quality trade-off (larger = slower, better).

### Pedigree (trio) phasing with constant recombination rate
**Args:** `whatshap phase --ped trio.ped --recombrate 1.0 -r ref.fa -o phased_trio.vcf trio.vcf child.bam father.bam mother.bam`
**Explanation:** `--ped trio.ped` enables pedigree phasing using parents' reads to disambiguate the child's haplotypes; `--recombrate 1.0` assumes 1 cM/Mb; all three BAMs are passed in any order — WhatsHap matches them to PED sample IDs via `@RG SM:`. PED columns: `FAM child father mother sex phenotype`.

### Pedigree phasing with genetic map
**Args:** `whatshap phase --ped trio.ped --genmap chr1.map -r ref.fa -o phased.vcf trio.vcf c.bam f.bam m.bam`
**Explanation:** `--genmap chr1.map` provides a position-resolved recombination map (one `pos cM` line per locus) instead of the constant `--recombrate`; produces more accurate block boundaries near recombination hotspots.

### Distrust genotypes and rescue mis-called variants
**Args:** `whatshap phase --distrust-genotypes --include-homozygous -r ref.fa -o phased.vcf calls.vcf aln.bam`
**Explanation:** `--distrust-genotypes` allows WhatsHap to flip hetero→homo (and vice versa) when reads strongly disagree with the called genotype; `--include-homozygous` includes homozygous variants in the dynamic programming (they don't usually help phasing but can anchor blocks). Use `--changed-genotype-list changed.txt` to log all flipped genotypes.

### Tag reads by haplotype (requires phased VCF)
**Args:** `whatshap haplotag -o tagged.bam -r ref.fa phased.vcf.gz aln.bam`
**Explanation:** `haplotag` adds `HP:i:1`/`HP:i:2` and `PS:i:<block>` SAM tags to each read; `phased.vcf.gz` **must** be bgzipped + `.tbi`-indexed (`bgzip` then `tabix -p vcf`); output BAM is coordinate-sorted and indexed automatically.

### Haplotag restricted to a region and write a haplotype list
**Args:** `whatshap haplotag --regions chr1:1000000-2000000 --output-haplotag-list hp.tsv -o tagged.bam phased.vcf.gz aln.bam`
**Explanation:** `--regions` limits tagging to reads overlapping the interval (speeds up large BAMs); `--output-haplotag-list hp.tsv` writes `read_name<TAB>haplotype` for downstream parsing.

### Handle supplementary alignments explicitly
**Args:** `whatshap haplotag --tag-supplementary independent-or-copy-primary -o tagged.bam phased.vcf.gz ont.bam`
**Explanation:** `--tag-supplementary independent-or-copy-primary` first attempts to assign the supplementary alignment independently; if it cannot decide, it copies the primary's tag. Alternatives: `skip` (no tag), `copy-primary` (always match primary), `independent-or-skip` (skip if undecided).

### Print phasing statistics and TSV report
**Args:** `whatshap stats --tsv stats.tsv --block-list blocks.txt phased.vcf > stats.txt`
**Explanation:** `stats` prints block count, # phased variants, NG50 etc. to stdout; `--tsv stats.tsv` writes the same metrics as machine-readable TSV; `--block-list blocks.txt` lists every phased block (one per line: `chrom start end sample nvariants`).

### Phasing statistics for a specific sample and SNVs only
**Args:** `whatshap stats --sample NA12878 --only-snvs --gtf blocks.gtf phased.vcf`
**Explanation:** `--sample NA12878` restricts to one sample in a multi-sample VCF; `--only-snvs` ignores indels in block-length calculations; `--gtf blocks.gtf` writes phased blocks as a GTF (one "gene" per block) for IGV/UCSC visualisation.

### Compare two phased VCFs
**Args:** `whatshap compare --output-comparison cmp.tsv a_phased.vcf b_phased.vcf`
**Explanation:** `compare` reports the switch-error rate and hamming distance between two phasings, useful for benchmarking against a truth set or across algorithms. Reads from both VCFs must use the same variant representation (left-normalised, single-allele per line).

### Remove phasing information from a VCF
**Args:** `whatshap unphase phased.vcf > unphased.vcf`
**Explanation:** `unphase` strips `PS`, `HP`, and `GT` phasing separators (`|`→`/`), useful before re-phasing or feeding tools that expect unphased genotypes.
