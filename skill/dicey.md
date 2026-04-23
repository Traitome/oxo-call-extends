---
name: dicey
category: utility
description: In-silico PCR and variant primer design.
tags: [dicey, utility, pcr, primer-design, in-silico]
author: oxo-call-community
source_url: "https://github.com/gear-genomics/dicey"
---

## Concepts

- **Tool Overview**: dicey v0.3.4 - Tool for in-silico PCR simulation and variant-aware primer design.
- **Core Function**: Simulates PCR reactions in silico and designs primers that account for known variants.
- **Input/Output**: Expects reference genome and primer sequences; outputs in-silico PCR products and primer designs.
- **Installation**: `conda install -c bioconda dicey`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires indexed reference genome.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dicey pcr --ref ref.fa --primers primers.tsv --output pcr_products.bed`
**Explanation:** Simulates in-silico PCR on reference genome.
