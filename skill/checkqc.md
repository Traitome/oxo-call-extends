---
name: checkqc
category: qc
description: A simple program to parse Illumina NGS data and check it for quality criteria.
tags: [checkqc, qc]
author: oxo-call-community
source_url: "https://checkqc.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: checkqc (v4.0.7) - A simple program to parse Illumina NGS data and check it for quality criteria.
- **Core Function**: A simple program to parse Illumina NGS data and check it for quality criteria.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda checkqc`

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
