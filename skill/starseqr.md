---
name: starseqr
category: expression
description: RNA Fusion Detection and Quantification
tags: [starseqr, expression]
author: oxo-call-community
source_url: "https://github.com/ExpressionAnalysis/STAR-SEQR"
---

## Concepts

- **Tool Overview**: starseqr (v0.6.7) - RNA Fusion Detection and Quantification
- **Core Function**: RNA Fusion Detection and Quantification
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda starseqr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `starseqr -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run starseqr with typical input and output options.
