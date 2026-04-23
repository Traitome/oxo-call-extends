---
name: grid
category: qc
description: Growth Rate Index (GRiD) measures bacterial growth rate from reference genomes (including draft quality genomes) and metagenomic bins at ultra-low sequencing coverage (> 0.2x).
tags: [grid, qc]
author: oxo-call-community
source_url: "https://github.com/ohlab/GRiD"
---

## Concepts

- **Tool Overview**: grid (v1.3) - Growth Rate Index (GRiD) measures bacterial growth rate from reference genomes (including draft quality genomes) and metagenomic bins at ultra-low sequencing coverage (> 0.2x).
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda grid`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
