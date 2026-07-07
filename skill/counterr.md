---
name: counterr
category: utility
description: Light-weight tool to compute sequencing errors by comparing reads to reference
tags: [counterr, sequencing-errors, quality-control, reference-comparison, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dayzerodx/counterr"
---

## Concepts

- **Tool Overview**: Counterr is a lightweight command-line tool that computes sequencing errors by comparing reads to a reference genome, providing detailed error analysis.
- **Core Function**: Identifies and quantifies sequencing errors by aligning reads to a reference and counting mismatches, insertions, and deletions.
- **Algorithm**: Maps reads to reference and calculates error rates at each position, providing base-level error statistics.
- **Input**: Sequencing reads (FASTQ), reference genome (FASTA).
- **Output**: Error statistics, per-base error rates, error profiles.
- **Application**: Sequencing quality control, error rate estimation, data validation.
- **Installation**: Install via bioconda: `conda install -c bioconda counterr`

## Pitfalls

- **Mapping Quality**: Requires accurate read mapping for reliable error detection.
- **Reference Quality**: Errors in reference genome affect error estimation.
- **Read Length**: Short reads may provide limited error information.
- **Coverage Depth**: Low coverage affects statistical significance.
- **Indel Handling**: May have limitations in complex indel regions.

## Examples

### Compute sequencing errors
**Args:** `counterr -i reads.fastq -r reference.fasta -o error_report.txt`
**Explanation:** Computes sequencing errors by comparing reads to reference.

### With paired reads
**Args:** `counterr -1 reads_1.fastq -2 reads_2.fastq -r reference.fasta -o error_report.txt`
**Explanation:** Analyzes paired-end reads for error detection.

### Output per-base errors
**Args:** `counterr -i reads.fastq -r reference.fasta --per-base -o per_base_errors.txt`
**Explanation:** Generates per-base error rate report.

### Filter by quality
**Args:** `counterr -i reads.fastq -r reference.fasta -q 20 -o error_report.txt`
**Explanation:** Filters reads by quality score before error analysis.

### Display help
**Args:** `counterr --help`
**Explanation:** Shows all available options and usage information.