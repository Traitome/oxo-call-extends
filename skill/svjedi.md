---
name: svjedi
category: variant-calling
description: SVJedi is a structural variation (SV) genotyper for long read data.
tags: [svjedi, variant-calling]
author: oxo-call-community
source_url: "https://github.com/llecompte/SVJedi"
---

## Concepts

- **Tool Overview**: svjedi (v1.1.6) - SVJedi is a structural variation (SV) genotyper for long read data.
- **Core Function**: SVJedi is a structural variation (SV) genotyper for long read data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svjedi`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svjedi -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svjedi with typical input and output options.
