---
name: themis
category: metagenomics
description: Themis: metagenomic profiler
tags: [themis, metagenomics]
author: oxo-call-community
source_url: "https://github.com/xujialupaoli/Themis"
---

## Concepts

- **Tool Overview**: themis (v0.1.0) - Themis: metagenomic profiler
- **Core Function**: Themis: metagenomic profiler
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda themis`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `themis -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run themis with typical input and output options.
