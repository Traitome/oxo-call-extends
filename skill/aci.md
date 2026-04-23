---
name: aci
category: qc
description: Amplicon Coverage Inspector for quantifying coverage depth in amplicon-based sequencing data
tags: [amplicon, coverage, depth, qc, sequencing, artic]
author: oxo-call-community
source_url: "https://github.com/erinyoung/ACI"
---

## Concepts

- **Tool Overview**: ACI (Amplicon Coverage Inspector) is a bioinformatics tool designed to quantify coverage depth in amplicon-based sequencing data (e.g., ARTIC, Midnight, Swift protocols).
- **Core Function**: Analyzes coverage depth for each amplicon in panel-based sequencing, identifying failed amplicons and generating visual reports.
- **Input/Output**: Input: BAM files and BED file with amplicon coordinates. Output: Coverage reports and visualizations in output directory.
- **Parallel Processing**: Supports multi-threading for sorting and counting, and can process multiple BAM files simultaneously.
- **Installation**: Install via bioconda: `conda install -c bioconda aci`

## Pitfalls

- **BED Format**: Requires 4-column BED file without header (chrom, start, end, amplicon_name).
- **BAM Sorting**: Automatically sorts BAM files if not already sorted - may create large temporary files.
- **Threshold Settings**: Default fail threshold (10x) may be too low for some applications - adjust based on coverage requirements.
- **Memory Usage**: Processing many large BAM files simultaneously may require significant memory.

## Examples

### Display help and version
**Args:** `--help`
**Explanation:** Shows all available command line options and their default values.

### Analyze single BAM file
**Args:** `--bam sample.bam --bed amplicons.bed --out results`
**Explanation:** Analyzes coverage for a single sample using the amplicon BED file, outputs to results directory.

### Analyze multiple BAM files
**Args:** `--bam sample1.bam sample2.bam sample3.bam --bed amplicons.bed --out results`
**Explanation:** Processes multiple samples in one run, generating comparative coverage reports.

### Process with wildcards
**Args:** `--bam *.bam --bed amplicons.bed --out results`
**Explanation:** Automatically processes all BAM files in current directory.

### Custom coverage threshold
**Args:** `--bam sample.bam --bed amplicons.bed --fail-threshold 100 --out results`
**Explanation:** Sets minimum coverage threshold to 100x for amplicon pass/fail determination.

### Adjust fail percentage
**Args:** `--bam sample.bam --bed amplicons.bed --fail-percentage 30 --out results`
**Explanation:** Marks amplicons as failed only if >30% of samples fail the threshold (default 50%).

### Multi-threaded processing
**Args:** `--bam *.bam --bed amplicons.bed --threads 8 --out results`
**Explanation:** Uses 8 threads for parallel processing of BAM sorting and coverage counting.

### Custom temporary directory
**Args:** `--bam sample.bam --bed amplicons.bed --tmpdir /scratch/tmp --out results`
**Explanation:** Uses custom temporary directory for intermediate files, useful for limited disk space.
