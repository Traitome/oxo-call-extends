---
name: scsplit
category: variant-calling
description: Genotype-free demultiplexing of pooled single-cell RNA-Seq
tags: [scsplit, variant-calling]
author: oxo-call-community
source_url: "https://github.com/jon-xu/scSplit"
---

## Concepts

- **Tool Overview**: scsplit (v1.0.8.2) - Genotype-free demultiplexing of pooled single-cell RNA-Seq
- **Core Function**: Genotype-free demultiplexing of pooled single-cell RNA-Seq
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scsplit`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scsplit -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run scsplit with typical input and output options.
