---
name: scvelo
category: utility
description: single-cell RNA velocity generalized to transient cell states
tags: [scvelo, utility]
author: oxo-call-community
source_url: "https://github.com/theislab/scvelo"
---

## Concepts

- **Tool Overview**: scvelo (v0.2.5) - single-cell RNA velocity generalized to transient cell states
- **Core Function**: single-cell RNA velocity generalized to transient cell states
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scvelo`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scvelo -i <input_file> -o <output_file>`
**Explanation:** Run scvelo with typical input and output options.
