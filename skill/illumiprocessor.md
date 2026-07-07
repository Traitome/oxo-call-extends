---
name: illumiprocessor
category: qc
description: illumiprocessor is a tool to batch process illumina sequencing reads using the excellent trimmomatic package.
tags: [illumiprocessor, qc, trimmomatic, trimming]
author: oxo-call-community
source_url: "https://github.com/faircloth-lab/illumiprocessor"
---

## Concepts

- **Tool Overview**: illumiprocessor (v2.10) - A batch processing tool for Illumina sequencing reads that wraps Trimmomatic for quality trimming and adapter removal
- **Core Function**: Automates parallel processing of multiple Illumina samples with configurable trimming parameters
- **Input/Output**: Accepts raw FASTQ files, outputs trimmed reads and quality reports
- **Installation**: `conda install -c bioconda illumiprocessor` or from GitHub
- **Configuration**: Uses INI-style configuration files for batch processing setup

## Pitfalls

- **Trimmomatic Dependency**: Requires Trimmomatic to be installed and accessible
- **Configuration Format**: Strict INI file format; incorrect syntax causes failures
- **Adapter Selection**: Choosing wrong adapter sequences leads to incomplete trimming
- **Parallel Processing**: Thread count should match available CPU cores
- **Output Organization**: Requires careful directory structure for proper output

## Examples

### Run basic batch processing
**Args:** `illumiprocessor --input config.ini --output results/`
**Explanation:** Processes all samples defined in config.ini using default Trimmomatic settings.

### Custom trimming parameters
**Args:** `illumiprocessor --input config.ini --output results/ --trimmer LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36`
**Explanation:** Specifies custom trimming parameters for quality filtering.

### Specify adapter file
**Args:** `illumiprocessor --input config.ini --output results/ --adapters TruSeq3-PE.fa`
**Explanation:** Uses custom adapter sequences from specified FASTA file.

### Run in parallel
**Args:** `illumiprocessor --input config.ini --output results/ --threads 8`
**Explanation:** Processes 8 samples in parallel using 8 threads.

### Single-end mode
**Args:** `illumiprocessor --input config.ini --output results/ --single-end`
**Explanation:** Processes single-end reads instead of paired-end.

### Generate trimming report
**Args:** `illumiprocessor --input config.ini --output results/ --report`
**Explanation:** Generates comprehensive trimming statistics report.