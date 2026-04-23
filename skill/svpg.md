---
name: svpg
category: variant-calling
description: Pangenome-based structural variation caller
tags: [svpg, variant-calling]
author: oxo-call-community
source_url: "https://github.com/coopsor/SVPG"
---

## Concepts

- **Tool Overview**: svpg (v1.4.1) - Pangenome-based structural variation caller
- **Core Function**: Pangenome-based structural variation caller
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svpg`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svpg -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svpg with typical input and output options.
