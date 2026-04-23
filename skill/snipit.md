---
name: snipit
category: variant-calling
description: Visualize snps relative to a reference sequence
tags: [snipit, variant-calling]
author: oxo-call-community
source_url: "https://github.com/aineniamh/snipit"
---

## Concepts

- **Tool Overview**: snipit (v1.7) - Visualize snps relative to a reference sequence
- **Core Function**: Visualize snps relative to a reference sequence
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snipit`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snipit -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run snipit with typical input and output options.
