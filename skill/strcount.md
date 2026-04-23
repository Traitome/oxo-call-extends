---
name: strcount
category: expression
description: A package to count the number of repeats in a Short Tandem Repeat Expansion from long reads.
tags: [strcount, expression]
author: oxo-call-community
source_url: "https://github.com/sabiqali/strcount"
---

## Concepts

- **Tool Overview**: strcount (v0.1.1) - A package to count the number of repeats in a Short Tandem Repeat Expansion from long reads.
- **Core Function**: A package to count the number of repeats in a Short Tandem Repeat Expansion from long reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strcount`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strcount -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run strcount with typical input and output options.
