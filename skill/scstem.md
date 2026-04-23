---
name: scstem
category: alignment
description: A method for mapping single-cell and spatial transcriptomics data with transfer learning
tags: [scstem, alignment]
author: oxo-call-community
source_url: "https://github.com/WhirlFirst/STEM"
---

## Concepts

- **Tool Overview**: scstem (v0.0.2) - A method for mapping single-cell and spatial transcriptomics data with transfer learning
- **Core Function**: A method for mapping single-cell and spatial transcriptomics data with transfer learning
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scstem`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scstem -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run scstem with typical input and output options.
