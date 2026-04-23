---
name: secedo
category: hpc
description: SNV-based clustering for single-cell sequencing data.
tags: [secedo, hpc]
author: oxo-call-community
source_url: "https://github.com/ratschlab/secedo"
---

## Concepts

- **Tool Overview**: secedo (v1.0.7) - SNV-based clustering for single-cell sequencing data.
- **Core Function**: SNV-based clustering for single-cell sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda secedo`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `secedo -i <input_file> -o <output_file>`
**Explanation:** Run secedo with typical input and output options.
