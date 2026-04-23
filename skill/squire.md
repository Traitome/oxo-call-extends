---
name: squire
category: expression
description: Quantitative, locus-specific view of transposable element expression.
tags: [squire, expression]
author: oxo-call-community
source_url: "https://github.com/wyang17/SQuIRE"
---

## Concepts

- **Tool Overview**: squire (v0.9.9.92) - Quantitative, locus-specific view of transposable element expression.
- **Core Function**: Quantitative, locus-specific view of transposable element expression.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda squire`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `squire -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run squire with typical input and output options.
