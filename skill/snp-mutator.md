---
name: snp-mutator
category: variant-calling
description: Generate mutated sequence files from a reference genome.
tags: [snp-mutator, variant-calling]
author: oxo-call-community
source_url: "https://github.com/CFSAN-Biostatistics/snp-mutator"
---

## Concepts

- **Tool Overview**: snp-mutator (v1.2.0) - Generate mutated sequence files from a reference genome.
- **Core Function**: Generate mutated sequence files from a reference genome.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snp-mutator`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snp-mutator -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run snp-mutator with typical input and output options.
