---
name: tin-score-calculation
category: expression
description: Given a set of BAM files and a gene annotation BED file, calculates the Transcript Integrity Number (TIN) for each transcript.
tags: [tin-score-calculation, expression, bam, bed]
author: oxo-call-community
source_url: "The package home page"
---

## Concepts

- **Tool Overview**: tin-score-calculation (v0.6.3) - Given a set of BAM files and a gene annotation BED file, calculates the Transcript Integrity Number (TIN) for each transcript.
- **Core Function**: Given a set of BAM files and a gene annotation BED file, calculates the Transcript Integrity Number (TIN) for each transcript.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tin-score-calculation`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tin-score-calculation -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run tin-score-calculation with typical input and output options.
