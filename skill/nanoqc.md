---
name: nanoqc
category: qc
description: Create fastQC-like plots for Oxford Nanopore sequencing data.
tags: [nanoqc, qc, nanopore, fastqc, visualization]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanoQC"
---

## Concepts

- **Tool Overview**: NanoQC v0.10.0 - fastQC-like plots for Nanopore sequencing data.
- **Core Function**: Generates quality control plots similar to FastQC but optimized for Nanopore data.
- **Input/Output**: Takes FASTQ or sequencing_summary.txt; outputs HTML QC plots.
- **Installation**: `conda install -c bioconda nanoqc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports FASTQ and sequencing summary formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq.gz -o output_dir`
**Explanation:** Generates fastQC-like plots for Nanopore data.
