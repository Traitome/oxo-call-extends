---
name: scramble
category: alignment
description: Soft Clipped Read Alignment Mapper
tags: [scramble, alignment]
author: oxo-call-community
source_url: "https://github.com/GeneDx/scramble"
---

## Concepts

- **Tool Overview**: scramble (v1.0.2) - Soft Clipped Read Alignment Mapper
- **Core Function**: Soft Clipped Read Alignment Mapper
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scramble`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scramble -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run scramble with typical input and output options.
