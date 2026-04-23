---
name: svaba
category: variant-calling
description: Structural variation and indel detection by local assembly
tags: [svaba, variant-calling]
author: oxo-call-community
source_url: "https://github.com/walaj/svaba"
---

## Concepts

- **Tool Overview**: svaba (v1.2.0) - Structural variation and indel detection by local assembly
- **Core Function**: Structural variation and indel detection by local assembly
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svaba`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svaba -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svaba with typical input and output options.
