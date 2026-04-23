---
name: svync
category: variant-calling
description: A tool to standardize VCF files from structural variant callers
tags: [svync, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/nvnieuwk/svync"
---

## Concepts

- **Tool Overview**: svync (v0.3.0) - A tool to standardize VCF files from structural variant callers
- **Core Function**: A tool to standardize VCF files from structural variant callers
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svync`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svync -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svync with typical input and output options.
