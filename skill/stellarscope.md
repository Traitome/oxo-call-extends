---
name: stellarscope
category: annotation
description: Single-cell Transposable Element Locus Level Analysis of scRNA Sequencing.
tags: [stellarscope, annotation]
author: oxo-call-community
source_url: "https://github.com/nixonlab/stellarscope/blob/1.5/docs/protocol.md"
---

## Concepts

- **Tool Overview**: stellarscope (v1.5) - Single-cell Transposable Element Locus Level Analysis of scRNA Sequencing.
- **Core Function**: Single-cell Transposable Element Locus Level Analysis of scRNA Sequencing.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stellarscope`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stellarscope -i <input.fasta> -o <output.gff>`
**Explanation:** Run stellarscope with typical input and output options.
