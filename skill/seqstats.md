---
name: seqstats
category: utility
description: Quick summary statistics on fasta/fastq(.gz) files
tags: [seqstats, utility, fasta, fastq]
author: oxo-call-community
source_url: "https://github.com/clwgg/seqstats"
---

## Concepts

- **Tool Overview**: seqstats (v1.0.0) - Quick summary statistics on fasta/fastq(.gz) files
- **Core Function**: Quick summary statistics on fasta/fastq(.gz) files
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqstats`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqstats -i <input_file> -o <output_file>`
**Explanation:** Run seqstats with typical input and output options.
