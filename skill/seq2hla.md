---
name: seq2hla
category: expression
description: Precision HLA typing and expression from next-generation RNA sequencing data
tags: [seq2hla, expression]
author: oxo-call-community
source_url: "https://github.com/TRON-Bioinformatics/seq2HLA"
---

## Concepts

- **Tool Overview**: seq2hla (v2.3) - Precision HLA typing and expression from next-generation RNA sequencing data
- **Core Function**: Precision HLA typing and expression from next-generation RNA sequencing data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seq2hla`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seq2hla -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run seq2hla with typical input and output options.
