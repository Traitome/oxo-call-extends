---
name: tecount
category: alignment
description: A package to count read alignments on transposable elements subfamilies, families and classes.
tags: [tecount, alignment]
author: oxo-call-community
source_url: "https://github.com/bodegalab/tecount"
---

## Concepts

- **Tool Overview**: tecount (v1.0.1) - A package to count read alignments on transposable elements subfamilies, families and classes.
- **Core Function**: A package to count read alignments on transposable elements subfamilies, families and classes.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tecount`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tecount -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run tecount with typical input and output options.
