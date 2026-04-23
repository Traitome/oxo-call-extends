---
name: strdust
category: variant-calling
description: Tandem repeat genotyper for long reads.
tags: [strdust, variant-calling]
author: oxo-call-community
source_url: "https://github.com/wdecoster/STRdust/blob/v0.16.0/README.md"
---

## Concepts

- **Tool Overview**: strdust (v0.16.0) - Tandem repeat genotyper for long reads.
- **Core Function**: Tandem repeat genotyper for long reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strdust`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strdust -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run strdust with typical input and output options.
