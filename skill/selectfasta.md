---
name: selectfasta
category: utility
description: FASTA or FASTQ select from a list of header names
tags: [selectfasta, utility, fasta, fastq]
author: oxo-call-community
source_url: "https://github.com/andvides/selectFasta/"
---

## Concepts

- **Tool Overview**: selectfasta (v3.1) - FASTA or FASTQ select from a list of header names
- **Core Function**: FASTA or FASTQ select from a list of header names
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda selectfasta`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `selectfasta -i <input_file> -o <output_file>`
**Explanation:** Run selectfasta with typical input and output options.
