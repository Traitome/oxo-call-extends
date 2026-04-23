---
name: strike
category: alignment
description: A program to evaluate protein multiple sequence alignments using a single protein structure.
tags: [strike, alignment]
author: oxo-call-community
source_url: "http://www.tcoffee.org/Projects/strike/index.html"
---

## Concepts

- **Tool Overview**: strike (v1.2) - A program to evaluate protein multiple sequence alignments using a single protein structure.
- **Core Function**: A program to evaluate protein multiple sequence alignments using a single protein structure.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strike`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strike -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run strike with typical input and output options.
