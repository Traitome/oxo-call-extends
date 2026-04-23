---
name: souporcell
category: variant-calling
description: Clustering scRNAseq by genotypes.
tags: [souporcell, variant-calling]
author: oxo-call-community
source_url: "https://github.com/wheaton5/souporcell"
---

## Concepts

- **Tool Overview**: souporcell (v2.5) - Clustering scRNAseq by genotypes.
- **Core Function**: Clustering scRNAseq by genotypes.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda souporcell`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `souporcell -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run souporcell with typical input and output options.
