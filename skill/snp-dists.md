---
name: snp-dists
category: alignment
description: Convert a FASTA alignment to SNP distance matrix.
tags: [snp-dists, alignment, fasta]
author: oxo-call-community
source_url: "https://github.com/tseemann/snp-dists"
---

## Concepts

- **Tool Overview**: snp-dists (v1.2.0) - Convert a FASTA alignment to SNP distance matrix.
- **Core Function**: Convert a FASTA alignment to SNP distance matrix.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snp-dists`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snp-dists -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run snp-dists with typical input and output options.
