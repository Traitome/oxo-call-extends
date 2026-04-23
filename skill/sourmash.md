---
name: sourmash
category: utility
description: Quickly search, compare, and analyze genomic and metagenomic data sets.
tags: [sourmash, utility]
author: oxo-call-community
source_url: "https://sourmash.readthedocs.io/"
---

## Concepts

- **Tool Overview**: sourmash (v4.9.4) - Quickly search, compare, and analyze genomic and metagenomic data sets.
- **Core Function**: Quickly search, compare, and analyze genomic and metagenomic data sets.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sourmash`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sourmash -i <input_file> -o <output_file>`
**Explanation:** Run sourmash with typical input and output options.
