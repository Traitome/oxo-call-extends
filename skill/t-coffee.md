---
name: t-coffee
category: alignment
description: A collection of tools for Multiple Alignments of DNA, RNA, Protein Sequence.
tags: [t-coffee, alignment]
author: oxo-call-community
source_url: "https://tcoffee.org/Projects/tcoffee/documentation/index.html"
---

## Concepts

- **Tool Overview**: t-coffee (v13.46.2.7c9e712d) - A collection of tools for Multiple Alignments of DNA, RNA, Protein Sequence.
- **Core Function**: A collection of tools for Multiple Alignments of DNA, RNA, Protein Sequence.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda t-coffee`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `t-coffee -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run t-coffee with typical input and output options.
