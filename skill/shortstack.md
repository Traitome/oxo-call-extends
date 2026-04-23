---
name: shortstack
category: expression
description: ShortStack: Comprehensive annotation and quantification of small RNA genes
tags: [shortstack, expression]
author: oxo-call-community
source_url: "https://github.com/MikeAxtell/ShortStack"
---

## Concepts

- **Tool Overview**: shortstack (v4.1.2) - ShortStack: Comprehensive annotation and quantification of small RNA genes
- **Core Function**: ShortStack: Comprehensive annotation and quantification of small RNA genes
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shortstack`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shortstack -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run shortstack with typical input and output options.
