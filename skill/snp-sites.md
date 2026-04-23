---
name: snp-sites
category: alignment
description: Finds SNP sites from a multi-FASTA alignment file.
tags: [snp-sites, alignment, fasta]
author: oxo-call-community
source_url: "https://sanger-pathogens.github.io/snp-sites"
---

## Concepts

- **Tool Overview**: snp-sites (v2.5.1) - Finds SNP sites from a multi-FASTA alignment file.
- **Core Function**: Finds SNP sites from a multi-FASTA alignment file.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snp-sites`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snp-sites -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run snp-sites with typical input and output options.
