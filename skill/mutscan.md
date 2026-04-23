---
name: mutscan
category: variant-calling
description: Detect and visualize target mutations by scanning FastQ files directly.
tags: [mutscan, variant-calling, mutation, fastq, visualization]
author: oxo-call-community
source_url: "https://github.com/OpenGene/MutScan"
---

## Concepts

- **Tool Overview**: MutScan v1.14.1 - detects and visualizes target mutations by scanning FastQ files directly.
- **Core Function**: Scans FASTQ files for known target mutations without requiring alignment, enabling rapid mutation screening.
- **Input/Output**: Takes FASTQ files and mutation definitions; outputs detected mutations with visualization.
- **Installation**: `conda install -c bioconda mutscan`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure FASTQ files are not compressed or provide gzipped FASTQ.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq.gz -m mutations.txt -o output_dir`
**Explanation:** Scans FASTQ file for target mutations and generates visualization.
