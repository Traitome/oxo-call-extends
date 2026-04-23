---
name: telescope
category: expression
description: Single locus resolution of Transposable ELEment expression.
tags: [telescope, expression]
author: oxo-call-community
source_url: "https://github.com/mlbendall/telescope"
---

## Concepts

- **Tool Overview**: telescope (v1.0.3) - Single locus resolution of Transposable ELEment expression.
- **Core Function**: Single locus resolution of Transposable ELEment expression.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda telescope`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `telescope -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run telescope with typical input and output options.
