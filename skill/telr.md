---
name: telr
category: annotation
description: A a fast non-reference transposable element (TE) detector from long read (LR) sequencing data (PacBio or Oxford Nanopore).
tags: [telr, annotation]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/telr"
---

## Concepts

- **Tool Overview**: telr (v1.1) - A a fast non-reference transposable element (TE) detector from long read (LR) sequencing data (PacBio or Oxford Nanopore).
- **Core Function**: A a fast non-reference transposable element (TE) detector from long read (LR) sequencing data (PacBio or Oxford Nanopore).
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda telr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `telr -i <input.fasta> -o <output.gff>`
**Explanation:** Run telr with typical input and output options.
