---
name: sneep
category: variant-calling
description: Identify regulatory non-coding SNPs (rSNPs)
tags: [sneep, variant-calling]
author: oxo-call-community
source_url: "https://github.com/SchulzLab/SNEEP"
---

## Concepts

- **Tool Overview**: sneep (v1.1) - Identify regulatory non-coding SNPs (rSNPs)
- **Core Function**: Identify regulatory non-coding SNPs (rSNPs)
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sneep`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sneep -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sneep with typical input and output options.
