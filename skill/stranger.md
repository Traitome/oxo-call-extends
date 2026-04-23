---
name: stranger
category: variant-calling
description: Annotate VCF files with STR variants with pathogenicity implications.
tags: [stranger, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/Clinical-Genomics/stranger/blob/v0.10.0/README.md"
---

## Concepts

- **Tool Overview**: stranger (v0.10.0) - Annotate VCF files with STR variants with pathogenicity implications.
- **Core Function**: Annotate VCF files with STR variants with pathogenicity implications.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stranger`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stranger -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run stranger with typical input and output options.
