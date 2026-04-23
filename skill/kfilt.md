---
name: kfilt
category: qc
description: A fast, multi-threaded tool for filtering FASTA/FASTQ reads based on k-mer matching using BK-trees.
tags: [kfilt, qc, FASTQ, FASTA]
author: oxo-call-community
source_url: "https://github.com/davidebolo1993/kfilt"
---

## Concepts

- **Tool Overview**: kfilt (v0.1.1) - A fast, multi-threaded tool for filtering FASTA/FASTQ reads based on k-mer matching using BK-trees.
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda kfilt`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
