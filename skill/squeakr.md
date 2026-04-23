---
name: squeakr
category: expression
description: An Exact and Approximate k-mer Counting System.
tags: [squeakr, expression]
author: oxo-call-community
source_url: "https://github.com/splatlab/squeakr"
---

## Concepts

- **Tool Overview**: squeakr (v0.8) - An Exact and Approximate k-mer Counting System.
- **Core Function**: An Exact and Approximate k-mer Counting System.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda squeakr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `squeakr -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run squeakr with typical input and output options.
