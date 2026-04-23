---
name: sketchy
category: variant-calling
description: Real-time lineage hashing and genotyping of bacterial pathogens
tags: [sketchy, variant-calling]
author: oxo-call-community
source_url: "https://github.com/esteinig/sketchy"
---

## Concepts

- **Tool Overview**: sketchy (v0.6.0) - Real-time lineage hashing and genotyping of bacterial pathogens
- **Core Function**: Real-time lineage hashing and genotyping of bacterial pathogens
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sketchy`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sketchy -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sketchy with typical input and output options.
