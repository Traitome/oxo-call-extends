---
name: seqwish
category: alignment
description: Alignment to variation graph inducer
tags: [seqwish, alignment]
author: oxo-call-community
source_url: "https://github.com/ekg/seqwish"
---

## Concepts

- **Tool Overview**: seqwish (v0.7.11) - Alignment to variation graph inducer
- **Core Function**: Alignment to variation graph inducer
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqwish`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqwish -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run seqwish with typical input and output options.
