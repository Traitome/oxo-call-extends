---
name: sibeliaz
category: alignment
description: A fast whole-genome aligner based on de Bruijn graphs.
tags: [sibeliaz, alignment]
author: oxo-call-community
source_url: "https://github.com/medvedevgroup/SibeliaZ/blob/v1.2.7/README.md"
---

## Concepts

- **Tool Overview**: sibeliaz (v1.2.7) - A fast whole-genome aligner based on de Bruijn graphs.
- **Core Function**: A fast whole-genome aligner based on de Bruijn graphs.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sibeliaz`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sibeliaz -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run sibeliaz with typical input and output options.
