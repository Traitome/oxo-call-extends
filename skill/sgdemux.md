---
name: sgdemux
category: utility
description: Tool for demultiplexing sequencing data generated on Singular Genomics' sequencing instruments.
tags: [sgdemux, utility]
author: oxo-call-community
source_url: "https://github.com/Singular-Genomics/singular-demux"
---

## Concepts

- **Tool Overview**: sgdemux (v1.2.0) - Tool for demultiplexing sequencing data generated on Singular Genomics' sequencing instruments.
- **Core Function**: Tool for demultiplexing sequencing data generated on Singular Genomics' sequencing instruments.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sgdemux`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sgdemux -i <input_file> -o <output_file>`
**Explanation:** Run sgdemux with typical input and output options.
