---
name: alignlib-lite
category: alignment
description: Simple wrapper around alignlib C++ library for sequence alignment.
tags: [alignlib-lite, alignment]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/alignlib"
---

## Concepts

- **Tool Overview**: alignlib-lite (v0.3) - Simple wrapper around alignlib C++ library for sequence alignment.
- **Core Function**: Simple wrapper around alignlib C++ library for sequence alignment.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda alignlib-lite`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
