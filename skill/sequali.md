---
name: sequali
category: qc
description: Fast sequencing quality metrics
tags: [sequali, qc]
author: oxo-call-community
source_url: "sequali.readthedocs.io"
---

## Concepts

- **Tool Overview**: sequali (v1.0.2) - Fast sequencing quality metrics
- **Core Function**: Fast sequencing quality metrics
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sequali`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sequali -i <input.fastq> -o <output_dir>`
**Explanation:** Run sequali with typical input and output options.
