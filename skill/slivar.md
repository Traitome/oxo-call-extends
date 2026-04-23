---
name: slivar
category: variant-calling
description: filter/annotate variants in VCF/BCF format with simple expressions.
tags: [slivar, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/brentp/slivar/blob/v0.3.3/README.md"
---

## Concepts

- **Tool Overview**: slivar (v0.3.3) - filter/annotate variants in VCF/BCF format with simple expressions.
- **Core Function**: filter/annotate variants in VCF/BCF format with simple expressions.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda slivar`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `slivar -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run slivar with typical input and output options.
