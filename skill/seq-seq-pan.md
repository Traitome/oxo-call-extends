---
name: seq-seq-pan
category: alignment
description: seq-seq-pan
tags: [seq-seq-pan, alignment]
author: oxo-call-community
source_url: "https://gitlab.com/chrjan/seq-seq-pan"
---

## Concepts

- **Tool Overview**: seq-seq-pan (v1.1.0) - seq-seq-pan
- **Core Function**: seq-seq-pan
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seq-seq-pan`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seq-seq-pan -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run seq-seq-pan with typical input and output options.
