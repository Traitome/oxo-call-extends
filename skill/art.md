---
name: art
category: qc
description: Illumina, 454 and Solid read simulator
tags: [art, qc]
author: oxo-call-community
source_url: "http://www.niehs.nih.gov/research/resources/software/biostatistics/art/"
---

## Concepts

- **Tool Overview**: art (v2016.06.05) - Illumina, 454 and Solid read simulator
- **Core Function**: Illumina, 454 and Solid read simulator
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda art`

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
