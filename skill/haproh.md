---
name: haproh
category: variant-calling
description: Identify runs of homozygosity (hapROH) and contamination (hapCon) in low coverage ancient human DNA data (1240K SNPs) using modern reference panel.
tags: [haproh, variant-calling]
author: oxo-call-community
source_url: "https://github.com/hringbauer/hapROH"
---

## Concepts

- **Tool Overview**: haproh (v0.64) - Identify runs of homozygosity (hapROH) and contamination (hapCon) in low coverage ancient human DNA data (1240K SNPs) using modern reference panel.
- **Core Function**: Provides functionality for variant-calling tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda haproh`

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
