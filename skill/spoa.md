---
name: spoa
category: alignment
description: SIMD partial order alignment tool/library.
tags: [spoa, alignment]
author: oxo-call-community
source_url: "https://github.com/rvaser/spoa/blob/4.1.5/README.md"
---

## Concepts

- **Tool Overview**: spoa (v4.1.5) - SIMD partial order alignment tool/library.
- **Core Function**: SIMD partial order alignment tool/library.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spoa`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spoa -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run spoa with typical input and output options.
