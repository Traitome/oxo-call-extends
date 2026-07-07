---
name: bactopia-qc
category: qc
description: Bactopia QC - Quality control component for Bactopia pipeline
tags: [bactopia-qc, qc, quality-control, fastqc, fastp, bacterial-genomics]
author: oxo-call-community
source_url: "https://bactopia.github.io/"
---

## Concepts

- **Tool Overview**: Bactopia QC is the quality control component of the Bactopia pipeline, providing comprehensive assessment of sequencing read quality. Version 1.0.4.
- **Core Function**: Performs quality control analysis on raw sequencing reads before assembly.
- **FastQC Integration**: Uses FastQC for comprehensive quality metric calculation.
- **fastp Integration**: Incorporates fastp for quality trimming and filtering.
- **Quality Reports**: Generates detailed HTML reports with quality metrics visualization.
- **Adapter Trimming**: Automatically detects and trims sequencing adapters.
- **Input/Output**: Accepts FASTQ reads, outputs quality reports and trimmed reads.
- **Installation**: `conda install -c bioconda bactopia-qc`.

## Pitfalls

- **Version Compatibility**: Must match Bactopia pipeline version for proper integration.
- **Read Quality**: Very poor quality reads may need additional preprocessing.
- **Adapter Detection**: May not detect custom adapters. Specify adapters if needed.
- **Memory Usage**: Large datasets require sufficient memory for quality analysis.

## Examples

### Basic quality control
**Args:** `bactopia-qc --input R1.fastq.gz R2.fastq.gz --output qc_results/`
**Explanation:** Runs complete QC analysis on paired-end reads.

### With trimming
**Args:** `bactopia-qc --input R1.fastq.gz R2.fastq.gz --trim --output qc_results/`
**Explanation:** Performs quality trimming in addition to QC analysis.

### Single-end reads
**Args:** `bactopia-qc --input reads.fastq.gz --single-end --output qc_results/`
**Explanation:** Processes single-end sequencing reads.

### Custom adapter sequence
**Args:** `bactopia-qc --input R1.fastq.gz R2.fastq.gz --adapter AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC --output qc_results/`
**Explanation:** Specifies custom adapter sequence for trimming.

### Quality threshold
**Args:** `bactopia-qc --input R1.fastq.gz R2.fastq.gz --min-quality 20 --output qc_results/`
**Explanation:** Sets minimum quality threshold for trimming.

### Generate report only
**Args:** `bactopia-qc --input R1.fastq.gz R2.fastq.gz --report-only --output qc_report.html`
**Explanation:** Generates QC report without trimming reads.

### Specify threads
**Args:** `bactopia-qc --input R1.fastq.gz R2.fastq.gz --threads 8 --output qc_results/`
**Explanation:** Uses specified number of threads for parallel processing.

### Display help
**Args:** `bactopia-qc --help`
**Explanation:** Shows all available command-line options and usage information.