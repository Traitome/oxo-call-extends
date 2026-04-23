---
name: confindr
category: qc
description: Detect intra- and inter-species bacterial contamination in NGS reads.
tags: [confindr, qc]
author: oxo-call-community
source_url: "https://OLC-Bioinformatics.github.io/ConFindr"
---

## Concepts

- **Tool Overview**: confindr (v0.8.2) - Detect intra- and inter-species bacterial contamination in NGS reads.
- **Core Function**: Detect intra- and inter-species bacterial contamination in NGS reads.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda confindr`

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
