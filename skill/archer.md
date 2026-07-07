---
name: archer
category: hpc
description: Archer - Pre-process amplicon data before running CLIMB workflows
tags: [archer, hpc, amplicon, preprocessing, climb, workflow]
author: oxo-call-community
source_url: "https://github.com/will-rowe/archer"
---

## Concepts

- **Tool Overview**: Archer is a tool for pre-processing amplicon sequencing data before running CLIMB (Cloud Infrastructure for Microbial Bioinformatics) workflows. Version 0.1.1.
- **Core Function**: Prepares amplicon data by performing quality control, adapter trimming, and format conversion for downstream analysis.
- **Amplicon Data**: Designed for targeted amplicon sequencing data (e.g., 16S rRNA, ITS, or custom amplicon panels).
- **CLIMB Integration**: Specifically designed to prepare data for CLIMB cloud-based microbial bioinformatics workflows.
- **Quality Control**: Performs read quality filtering, adapter removal, and length trimming.
- **Input/Output**: Accepts FASTQ files and outputs processed FASTQ files ready for CLIMB workflows.
- **Installation**: `conda install -c bioconda archer` or build from GitHub.

## Pitfalls

- **Amplicon Specific**: Optimized for amplicon data. May not be suitable for whole-genome sequencing.
- **CLIMB Dependency**: Designed for CLIMB workflows. May require CLIMB-specific configurations.
- **Adapter Sequences**: Requires correct adapter sequences for trimming. Incorrect adapters cause data loss.
- **Quality Thresholds**: Stringent quality filtering may remove too many reads. Adjust thresholds based on data quality.
- **Batch Processing**: Large batches may require significant processing time and storage.

## Examples

### Display help
**Args:** `archer --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic preprocessing
**Args:** `archer preprocess --input reads.fastq --output processed_reads.fastq`
**Explanation:** Performs basic preprocessing including quality filtering and adapter trimming.

### Specify adapter sequences
**Args:** `archer preprocess --input reads.fastq --adapter AGATCGGAAGAGC --output trimmed.fastq`
**Explanation:** Trims specified adapter sequence from reads.

### Set quality threshold
**Args:** `archer preprocess --input reads.fastq --min_quality 20 --output filtered.fastq`
**Explanation:** Filters reads with minimum average quality score of 20.

### Trim read length
**Args:** `archer preprocess --input reads.fastq --trim_length 250 --output trimmed.fastq`
**Explanation:** Trims reads to specified length (250bp) for uniform amplicon length.

### Batch processing
**Args:** `archer batch --input_dir raw_data/ --output_dir processed_data/`
**Explanation:** Processes multiple FASTQ files in batch mode.

### Generate QC report
**Args:** `archer preprocess --input reads.fastq --qc_report qc_report.html --output processed.fastq`
**Explanation:** Generates HTML quality control report alongside processed data.