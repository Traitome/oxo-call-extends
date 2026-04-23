---
name: shark
category: alignment
description: Mapping-free filtering of useless RNA-Seq reads
tags: [shark, alignment]
author: oxo-call-community
source_url: "https://algolab.github.io/shark/"
---

## Concepts

- **Tool Overview**: shark (v1.2.0) - Mapping-free filtering of useless RNA-Seq reads
- **Core Function**: Mapping-free filtering of useless RNA-Seq reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shark`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shark -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run shark with typical input and output options.
