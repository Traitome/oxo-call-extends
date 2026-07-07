---
name: rna-seqc
category: expression
description: Fast QC and process-optimization metrics for RNA-Seq BAM files; computes coverage, gene-body coverage, rRNA contamination, library complexity, and per-gene read counts.
tags: ["rna-seqc", "rna-seq", "qc", "coverage", "rrna", "metrics", "getzlab"]
author: oxo-call-community
source_url: "https://github.com/getzlab/rnaseqc/blob/v2.4.2/README.md"
---

## Concepts

- **Tool Overview**: RNA-SeQC (v2.4.2, getzlab / Broad) is a Java-based tool for computing a comprehensive set of RNA-Seq quality-control metrics from a BAM file. It is the canonical QC tool for RNA-Seq in the Broad Institute's RNA-Seq pipeline and is widely used in The Cancer Genome Atlas (TCGA) production.
- **Core Function**: Takes one or more RNA-Seq BAMs (coordinate-sorted, indexed) plus a reference FASTA and a GTF, and produces: (1) per-sample metrics (total reads, mapped reads, rRNA fraction, median CV, gene-body coverage), (2) per-gene read counts (counts.txt), and (3) a downsampled BAI/BAM for IGV visualization. Output is a structured directory of TSVs plus a single HTML summary.
- **Algorithm**: Uses a Java-based BAM walker (Picard-style) that streams through the BAM and computes on-the-fly metrics. Gene-body coverage is computed per gene by binning the gene into 100 buckets and reporting the read density in each bucket. rRNA contamination is measured by aligning a sample of reads to an rRNA repeat reference.
- **Input Format**: One or more coordinate-sorted, indexed BAM files (`.bam` + `.bai`); a reference FASTA (must be the same build used for alignment); a GTF (must be coordinate-sorted and indexed with `tabix`). The rRNA reference is auto-detected by the GTF attribute `gene_biotype "rRNA"`.
- **Output Format**: A directory with `metrics.tsv` (per-sample, one column per sample, one row per metric), `counts.txt` (gene-by-sample count matrix), `geneBodyCoverage.curves.txt` (per-sample coverage curve), and `*.bam` (downsampled BAMs for IGV, one per sample).
- **Use Case**: TCGA-style RNA-Seq QC for cohort analyses, validating a new library prep on a known cell line (e.g., checking that the gene-body coverage curve is flat), and identifying samples with high rRNA contamination or low library complexity before downstream analysis.

## Pitfalls

- **CRITICAL — Java 8/11/17 compatibility**: RNA-SeQC v2 is built against Java 8; running with Java 17+ produces a `NoSuchMethodError` from the Picard internals. Set `JAVA_HOME` to a Java 8/11 installation, or use the docker container `getlab/rnaseqc` to avoid the version mismatch.
- **CRITICAL — Reference FASTA must be the same build used for alignment**: A BAM aligned to GRCh38 cannot be QC'd against a GRCh37 reference FASTA — the gene coordinates will be wrong. The error message is generic ("gene not found") and easy to misdiagnose.
- **CRITICAL — GTF must be tabix-indexed**: The first step that fails on an unindexed GTF is the rRNA extraction; the failure mode is "GTF file not indexed", but it appears as a silent gene-body-coverage miss. Pre-process with `sort -k1,1 -k4,4n genes.gtf | bgzip > genes.gtf.gz && tabix -p gff genes.gtf.gz`.
- **The downsampled BAM is written to disk**: For large cohorts, this is hundreds of GB. Use `--output-directory` to a scratch disk with plenty of free space, and clean up the BAMs after IGV inspection (the metrics files are the actual deliverable).
- **`--rRNA` requires an explicit rRNA interval list**: The default behavior infers rRNA from the GTF `gene_biotype`, but if the GTF lacks this attribute, no rRNA metric is computed. Pass `--rRNA rrna.interval_list` with a Picard interval list of rRNA coordinates to force the metric.
- **Per-gene counts do not include multi-mapping reads**: For gene families with high sequence similarity (e.g., rRNA, histones), the counts are underestimated. Use Salmon/kallisto for these, or pre-filter with `samtools view -q 30`.

## Examples

### Standard QC run on a single sample
**Args:** `RNA-SeQC run --bam aligned.bam --reference ref.fa --gtf genes.gtf --output-directory sample1/`
**Explanation:** `--bam` is the coordinate-sorted BAM, `--reference` is the genome FASTA, `--gtf` is the annotation, `--output-directory` is where the metrics TSV, count matrix, and downsampled BAM are written. Java 8/11 must be active.

### QC a cohort
**Args:** `RNA-SeQC run --bam sample1.bam --bam sample2.bam --bam sample3.bam --reference ref.fa --gtf genes.gtf --output-directory cohort_qc/`
**Explanation:** Multiple `--bam` arguments are passed; the output `cohort_qc/metrics.tsv` has one column per sample. The gene-by-sample count matrix is written to `cohort_qc/counts.txt`.

### Use a custom rRNA interval list
**Args:** `RNA-SeQC run --bam aligned.bam --reference ref.fa --gtf genes.gtf --rRNA rrna.interval_list --output-directory sample1/`
**Explanation:** `--rRNA` provides a Picard interval list of rRNA coordinates; required when the GTF lacks the `gene_biotype` attribute. The rRNA fraction metric will appear in `metrics.tsv` under the `rRNA_pct` row.

### Skip the downsampled BAM
**Args:** `RNA-SeQC run --bam aligned.bam --reference ref.fa --gtf genes.gtf --output-directory sample1/ --no-bam-output`
**Explanation:** `--no-bam-output` (or `--skip-bam`) skips writing the downsampled BAM, saving disk space. Use this for large cohorts when IGV inspection is not needed.

### Set memory and threads
**Args:** `RNA-SeQC run --bam aligned.bam --reference ref.fa --gtf genes.gtf --output-directory sample1/ -Xmx16g -nct 8`
**Explanation:** `-Xmx16g` sets the JVM max heap to 16 GB; `-nct 8` uses 8 CPU threads. The default memory is 4 GB which is insufficient for whole-genome BAMs; raise to 8–32 GB for human-scale data.

### Output a single HTML report
**Args:** `RNA-SeQC run --bam aligned.bam --reference ref.fa --gtf genes.gtf --output-directory sample1/ --report-html sample1.html`
**Explanation:** `--report-html` writes a single self-contained HTML report combining all metrics; useful for emailing to a collaborator or attaching to a LIMS entry.

### Skip the per-gene count matrix
**Args:** `RNA-SeQC run --bam aligned.bam --reference ref.fa --gtf genes.gtf --output-directory sample1/ --skip-counts`
**Explanation:** `--skip-counts` omits the `counts.txt` count matrix; use this when you only need the QC metrics and will quantify with Salmon/kallisto separately.
