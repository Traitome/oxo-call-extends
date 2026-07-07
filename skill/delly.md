---
name: delly
category: variant-calling
description: Delly - integrated structural variant (SV) discovery, genotyping and CNV calling for short-read and long-read sequencing data.
tags: [delly, variant-calling, structural-variants, sv, cnv, paired-end, split-read, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dellytools/delly"
---

## Concepts

- **Tool Overview**: Delly (v2.0.x) is an integrated structural variant (SV) caller that uses paired-end, split-read and read-depth signals to discover, genotype and visualise deletions (DEL), tandem duplications (DUP), inversions (INV) and translocations (BND) at single-nucleotide resolution in short-read and long-read massively parallel sequencing data. C++ implementation; uses HTSlib, Boost and Edlib.
- **Subcommands** (`delly <command> <args>`):
  - `call` — short-read SV discovery + genotyping (paired-end + split-read).
  - `lr` — long-read SV discovery for PacBio HiFi (`-y pb`) or ONT (`-y ont`).
  - `cnv` — read-depth profiling and copy-number variant calling (requires mappability map).
  - `merge` — merge SV sites across VCF/BCF files into a unified site list.
  - `filter` / `classify` — filter somatic or germline SVs (`classify` is the newer name).
- **Input Requirements**:
  - BAM/CRAM: must be **sorted, indexed, and duplicate-marked** (use `picard MarkDuplicates` or `samtools markdup`).
  - Reference FASTA: must be indexed with `samtools faidx` for split-read realignment.
  - Mappability map (for `cnv`): downloadable from gear-genomics.embl.de/data/delly/ (e.g. `hg38.map.fa.gz`).
  - Exclude file (recommended): `-x hg38.excl` excludes telomeres, centromeres and unplaced contigs to avoid spurious calls.
- **SV Type Filtering**: `-t DEL|DUP|INV|BND|INS` restricts discovery to specific types. By default, all types are called.
- **Population Workflow** (germline):
  1. `delly call -g ref.fa -o s1.bcf -x hg38.excl sample1.bam` (per sample).
  2. `delly merge -o sites.bcf s1.bcf s2.bcf ... sN.bcf` (unify sites).
  3. `delly call -g ref.fa -v sites.bcf -o s1.geno.bcf -x hg38.excl sample1.bam` (genotype each sample at unified sites).
  4. `bcftools merge -m id -O b -o merged.bcf *.geno.bcf` (cohort VCF).
  5. `delly filter -f germline -o germline.bcf merged.bcf` (requires ≥20 unrelated samples).
- **Somatic Workflow** (tumor/control):
  1. `delly call -x hg38.excl -o t1.bcf -g hg38.fa tumor1.bam control1.bam`.
  2. `delly filter -f somatic -o t1.pre.bcf -s samples.tsv t1.bcf` (samples.tsv: `sample_id\ttumor|control`).
  3. `delly call -g hg38.fa -v t1.pre.bcf -o geno.bcf -x hg38.excl tumor1.bam control1.bam ... controlN.bam` (genotype across control panel).
  4. `delly filter -f somatic -o t1.somatic.bcf -s samples.tsv geno.bcf` (final filter).
- **Long-Read Mode**: `delly lr -y ont` for ONT (R9/R10), `delly lr -y pb` for PacBio HiFi. Supports alternate alignments (pan-genome graphs via minigraph) using `-l align.config`.
- **CNV Calling**: `delly cnv` requires a mappability map and uses GC + mappability fragment correction. Output `.bcf` contains `RDCN` genotype field; `.cov.gz` for plotting via `R/rd.R`.
- **Minimum SV Size**: short-read ~300 bp (depends on insert-size SD); small indels ≥15 bp via soft-clipped reads. Long-read ≥30 bp.
- **Installation**: `conda install -c bioconda delly`, Docker (`dellytools/delly`), Singularity (`.sif`), or static binary from GitHub releases.
- **Use Case**: Germline SV discovery in population cohorts; somatic SV calling in cancer genomes; long-read SV calling for PacBio/ONT assemblies; CNV profiling.

## Pitfalls

- **BAM must be sorted, indexed, and duplicate-marked**. Without `.bai`/`.csi`, Delly crashes on random access. Without duplicate marking, PCR duplicates inflate read-depth signal, producing false DUP/CNV calls. Use `samtools sort`, `samtools index`, `samtools markdup` (or `picard MarkDuplicates`).
- **Reference FASTA must match alignment reference**. Delly realigns split-reads against `--ref`, so contig names and sequences must match the BAM. Using `hg38.fa` for a b37-aligned BAM silently drops SVs on contigs not shared.
- **Always pass `-x hg38.excl` (or species equivalent)**. Without an exclude file, Delly scans centromeres, telomeres and unplaced contigs, producing thousands of false positives and dramatically slowing run time. Exclude templates ship in the GitHub repo (`excludeTemplates/`).
- **`delly filter -f germline` needs ≥20 unrelated samples**. The germline filter uses population allele frequency across the merged VCF; below 20 samples the frequency estimate is unstable and the filter becomes too permissive.
- **Multi-mapping reads must be marked as secondary/supplementary**. Delly expects exactly two primary alignment records per paired-end. Soft-clipped split reads must have one primary record plus supplementary records; otherwise the genotyper counts the same read multiple times. This is the BWA/minimap2 default but check your aligner.
- **SV type `-t` is case-sensitive and uppercase**. `-t del` is silently ignored; the correct values are `DEL`, `DUP`, `INV`, `BND`, `INS`. Multiple types are comma-separated: `-t DEL,DUP`.
- **`delly lr` is the long-read entry point, not `delly call`**. Using `delly call` on PacBio/ONT BAMs misses long-read-specific signals (read length, CIGAR gaps). `-y ont` vs `-y pb` selects the appropriate error model.
- **Mappability map required for `delly cnv`**. Without `-m hg38.map`, `delly cnv` cannot normalise read depth and the BCF contains unnormalised counts. Maps are species-specific; download from gear-genomics.embl.de/data/delly/.
- **`delly call -v sites.bcf` is the genotyping mode**. Without `-v`, `delly call` discovers SVs in the input BAM only. To genotype a cohort at unified sites, first `delly merge`, then run `delly call -v sites.bcf` per sample.
- **`bcftools merge -m id` (not `-m both`)**. Delly SV IDs are stable; `-m id` merges by ID. `-m both` falls back to position-based merging and can split a single SV into two records.
- **Inter-chromosomal translocations use `INFO/CHR2`, not the two-record BND format**. Convert via `python scripts/delly2bnd.py -v delly.bcf -r hg38.fa -o delly.bnd.bcf` for tools that require BND records (e.g. Manta, SVIM).
- **`delly classify` is the new name for `delly filter`**. In v2.0+ the subcommand is `classify`; older versions use `filter`. Both accept `-f somatic|germline`.
- **CNV sensitivity depends on `-z`, `-t`, `-x`**. `-z` (window size, default 10000) controls segmentation granularity; smaller values increase sensitivity but add noise. `-t` (coverage threshold) and `-x` (excluded regions) tune the somatic SCNA calling.

## Examples

### Call SVs from a short-read BAM (single sample)
**Args:** `delly call -g hg38.fa -o sample.bcf -x hg38.excl sample.bam`
**Explanation:** `delly call` is the short-read SV caller; `-g hg38.fa` is the faidx-indexed reference used for split-read realignment; `-o sample.bcf` writes BCF (binary VCF, faster than text VCF); `-x hg38.excl` excludes centromeres/telomeres/unplaced contigs to suppress false positives; `sample.bam` must be sorted + indexed + duplicate-marked.

### Restrict discovery to a specific SV type (deletions only)
**Args:** `delly call -g hg38.fa -o dels.bcf -x hg38.excl -t DEL sample.bam`
**Explanation:** `-t DEL` restricts discovery to deletions only (valid types: `DEL`, `DUP`, `INV`, `BND`, `INS`); other SV types are skipped, reducing runtime and output size. Comma-separate for multiple types: `-t DEL,DUP`.

### Discover SVs from long reads (ONT or PacBio)
**Args:** `delly lr -y ont -o ont.bcf -g hg38.fa ont.bam`
**Explanation:** `delly lr` is the long-read SV caller (distinct from `delly call`); `-y ont` selects the Oxford Nanopore error model (use `-y pb` for PacBio HiFi); `-g hg38.fa` is the reference; `ont.bam` must be aligned with minimap2 (`-ax map-ont`). Long-read mode calls SVs ≥30 bp.

### Germline cohort workflow: per-sample calling, merge, re-genotype
**Args:** `delly call -g hg38.fa -o s1.bcf -x hg38.excl sample1.bam && delly call -g hg38.fa -o s2.bcf -x hg38.excl sample2.bam && delly merge -o sites.bcf s1.bcf s2.bcf && delly call -g hg38.fa -v sites.bcf -o s1.geno.bcf -x hg38.excl sample1.bam && delly call -g hg38.fa -v sites.bcf -o s2.geno.bcf -x hg38.excl sample2.bam && bcftools merge -m id -O b -o merged.bcf s1.geno.bcf s2.geno.bcf && delly filter -f germline -o germline.bcf merged.bcf`
**Explanation:** Per-sample `delly call` discovers SVs; `delly merge` unifies sites; `delly call -v sites.bcf` genotypes each sample at the unified sites; `bcftools merge -m id` merges by SV ID (not position); `delly filter -f germline` requires ≥20 unrelated samples for allele-frequency-based filtering.

### Somatic SV calling (tumor + matched control)
**Args:** `delly call -x hg38.excl -o t1.bcf -g hg38.fa tumor1.bam control1.bam && delly filter -f somatic -o t1.pre.bcf -s samples.tsv t1.bcf`
**Explanation:** `delly call` discovers SVs jointly in tumor and control; `-x hg38.excl` excludes low-complexity regions; `delly filter -f somatic` pre-filters somatic candidates using a `samples.tsv` file (columns: `sample_id\ttumor|control`). For final somatic filtering, genotype across a control panel: `delly call -g hg38.fa -v t1.pre.bcf -o geno.bcf -x hg38.excl tumor1.bam control1.bam ... controlN.bam && delly filter -f somatic -o t1.somatic.bcf -s samples.tsv geno.bcf`.

### Compute read-depth profile and call CNVs
**Args:** `delly cnv -g hg38.fa -m hg38.map -c out.cov.gz -o cnv.bcf sample.bam`
**Explanation:** `delly cnv` counts reads in 10 kb mappable windows and normalises by GC + mappability; `-m hg38.map` is the mappability map (download from gear-genomics.embl.de/data/delly/); `-c out.cov.gz` writes the per-window coverage for plotting; `-o cnv.bcf` writes CNV calls with `RDCN` genotype field. Plot with `Rscript R/rd.R out.cov.gz`.

### Somatic copy-number alterations (SCNAs)
**Args:** `delly cnv -u -z 10000 -o tumor.bcf -c tumor.cov.gz -g hg38.fa -m hg38.map tumor.bam && delly cnv -u -v tumor.bcf -o control.bcf -g hg38.fa -m hg38.map control.bam && bcftools merge -m id -O b -o tc.bcf tumor.bcf control.bcf && delly classify -p -f somatic -o somatic.bcf -s samples.tsv tc.bcf`
**Explanation:** `-u` enables tumor segmentation; `-z 10000` is the window size (bp); first call segments the tumor, then genotype those segments in the control; `bcftools merge -m id` aligns by ID; `delly classify -p -f somatic` performs paired tumor/control filtering using `samples.tsv`.

### Long-read SV calling with pan-genome graph alternate alignments
**Args:** `minimap2 -ax map-pb -L chm13.fa sample.fq.gz | samtools sort -o sample.chm13.bam && minigraph --vc -cx lr pangenome.gfa.gz sample.fq.gz > sample.gaf.gz && printf "sample.chm13.bam\tchm13.fa\nsample.gaf.gz\tpangenome.gfa.gz\n" > align.config && delly lr -y pb -o delly.bcf -g hg38.fa -l align.config sample.hg38.bam`
**Explanation:** `minimap2` aligns to an alternate linear reference (CHM13); `minigraph` aligns to a pan-genome graph; the `align.config` file (tab-separated: `path\treference`) tells Delly to filter out SVs present in the alternate alignments (reducing reference bias); SVs are reported in GRCh38 coordinates. Use for diverse populations where a single linear reference masks true variation.

### Filter SVs by size and quality for downstream analysis
**Args:** `bcftools view -i '(QUAL>=300) && ( ((SVTYPE=="INS") && (INFO/SVLEN>50)) || (SVTYPE=="BND") || ((INFO/END - POS)>50) )' delly.bcf > delly.filtered.vcf`
**Explanation:** `QUAL>=300` keeps high-confidence calls; the size filter excludes SVs <50 bp (matching typical GIAB truth-set thresholds); `INFO/SVLEN` for insertions, `INFO/END - POS` for deletions/duplications/inversions; `SVTYPE=="BND"` translocations have no length. Standard filter for benchmarking against GIAB.

### Convert inter-chromosomal translocations to BND format
**Args:** `python scripts/delly2bnd.py -v delly.bcf -r hg38.fa -o delly.bnd.bcf`
**Explanation:** Delly encodes translocations as single records with `INFO/CHR2` (the second chromosome). Some downstream tools (Manta, SVIM, AnnotSV) require the two-record breakend (BND) format. The `delly2bnd.py` script (shipped in Delly's `scripts/` directory) splits each translocation into two BND records.

### Plot normalized copy-number profile
**Args:** `delly cnv -g hg38.fa -m hg38.map -c out.cov.gz -o out.bcf -s stats.gz sample.bam && Rscript R/rd.R out.cov.gz`
**Explanation:** `-s stats.gz` writes GC-bias statistics; `R/rd.R` (shipped with Delly) plots the normalised read-depth profile and segments it. To overlay CNV calls: `bcftools query -f "%CHROM\t%POS\t%INFO/END\t%ID[\t%RDCN]\n" out.bcf > seg.bed && Rscript R/rd.R out.cov.gz seg.bed`.
