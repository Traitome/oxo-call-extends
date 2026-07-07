---
name: ezfastq
category: formatting
description: "Organize FASTQs by sample for analysis"
tags: [ezfastq, formatting, FASTQ, sequencing-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bioforensics/ezfastq/"
---

## Concepts

- **Tool Overview**: ezfastq is a tool for organizing and managing FASTQ files by sample for downstream analysis.
- **Core Function**: Sorts and organizes FASTQ files based on sample information, facilitating efficient data management.
- **Input/Output**: Input: FASTQ files (paired-end or single-end). Output: Organized directory structure, sample manifests.
- **Algorithm**: Parses file names and metadata to organize files into sample-specific directories.
- **Key Features**: FASTQ organization, paired-end support, sample manifest generation, batch processing, file renaming.
- **Installation**: `conda install -c bioconda ezfastq`

## Pitfalls

- **File Naming**: Requires consistent file naming conventions.
- **Sample Identification**: Depends on accurate sample identification in file names.
- **Format Compatibility**: Requires standard FASTQ format.
- **Memory Usage**: Large datasets may require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic organization
**Args:** `ezfastq organize -i fastq_files/ -o organized_samples/`
**Explanation:** Organizes FASTQ files by sample.

### Paired-end reads
**Args:** `ezfastq organize -i fastq_files/ -o organized_samples/ --paired-end`
**Explanation:** Handles paired-end sequencing data.

### Generate manifest
**Args:** `ezfastq organize -i fastq_files/ -o organized_samples/ --manifest manifest.csv`
**Explanation:** Generates sample manifest file.

### File renaming
**Args:** `ezfastq rename -i fastq_files/ -o renamed_files/ --pattern "{sample}_{read}.fastq"`
**Explanation:** Renames FASTQ files using custom pattern.

### Batch processing
**Args:** `ezfastq organize -i run_directories/ -o organized_samples/ --batch`
**Explanation:** Processes multiple sequencing runs in batch mode.