---
name: t1k
category: variant-calling
description: T1K is a versatile methods to genotype highly polymorphic genes (e.g. KIR, HLA) with RNA-seq, WGS or WES data.
tags: [t1k, variant-calling]
author: oxo-call-community
source_url: "https://github.com/mourisl/T1K/blob/v1.0.9/README.md"
---

## Concepts

- **Tool Overview**: t1k (v1.0.9) - T1K is a versatile methods to genotype highly polymorphic genes (e.g. KIR, HLA) with RNA-seq, WGS or WES data.
- **Core Function**: T1K is a versatile methods to genotype highly polymorphic genes (e.g. KIR, HLA) with RNA-seq, WGS or WES data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda t1k`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `t1k -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run t1k with typical input and output options.
