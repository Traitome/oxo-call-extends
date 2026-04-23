---
name: snpeff
category: variant-calling
description: Genetic variant annotation and effect prediction toolbox
tags: [snpeff, variant-calling]
author: oxo-call-community
source_url: "http://snpeff.sourceforge.net/"
---

## Concepts

- **Tool Overview**: snpeff (v5.4.0c) - Genetic variant annotation and effect prediction toolbox
- **Core Function**: Genetic variant annotation and effect prediction toolbox
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snpeff`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snpeff -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run snpeff with typical input and output options.
