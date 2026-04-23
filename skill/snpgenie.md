---
name: snpgenie
category: variant-calling
description: Program for estimating πN/πS, dN/dS, and other diversity measures from next-generation sequencing data
tags: [snpgenie, variant-calling]
author: oxo-call-community
source_url: "https://github.com/chasewnelson/SNPGenie"
---

## Concepts

- **Tool Overview**: snpgenie (v1.0) - Program for estimating πN/πS, dN/dS, and other diversity measures from next-generation sequencing data
- **Core Function**: Program for estimating πN/πS, dN/dS, and other diversity measures from next-generation sequencing data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snpgenie`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snpgenie -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run snpgenie with typical input and output options.
