---
name: swipe
category: utility
description: Tool for performing rapid local alignment searches in amino acid or nucleotide sequence databases. It is a highly optimized implementation of the Smith-Waterman algoritm using SIMD parallel computing technology available on common CPUs.
tags: [swipe, utility]
author: oxo-call-community
source_url: "http://dna.uio.no/swipe"
---

## Concepts

- **Tool Overview**: swipe (v2.1.1) - Tool for performing rapid local alignment searches in amino acid or nucleotide sequence databases. It is a highly optimized implementation of the Smith-Waterman algoritm using SIMD parallel computing technology available on common CPUs.
- **Core Function**: Tool for performing rapid local alignment searches in amino acid or nucleotide sequence databases. It is a highly optimized implementation of the Smith-Waterman algoritm using SIMD parallel computing technology available on common CPUs.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda swipe`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `swipe -i <input_file> -o <output_file>`
**Explanation:** Run swipe with typical input and output options.
