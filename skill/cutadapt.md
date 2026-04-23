---
name: cutadapt
category: qc
description: Trim adapters from high-throughput sequencing reads
tags: [cutadapt, qc]
author: oxo-call-community
source_url: "https://cutadapt.readthedocs.io/"
---

## Concepts

- **Tool Overview**: cutadapt (v5.2) - Trim adapters from high-throughput sequencing reads
- **Core Function**: Trim adapters from high-throughput sequencing reads
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cutadapt`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
