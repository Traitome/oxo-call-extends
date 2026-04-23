---
name: sonneityping
category: annotation
description: Sonneityping parses the output of mykrobe predict for Shigella sonnei
tags: [sonneityping, annotation]
author: oxo-call-community
source_url: "https://github.com/katholt/sonneityping"
---

## Concepts

- **Tool Overview**: sonneityping (v20210201) - Sonneityping parses the output of mykrobe predict for Shigella sonnei
- **Core Function**: Sonneityping parses the output of mykrobe predict for Shigella sonnei
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sonneityping`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sonneityping -i <input.fasta> -o <output.gff>`
**Explanation:** Run sonneityping with typical input and output options.
