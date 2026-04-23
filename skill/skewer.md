---
name: skewer
category: qc
description: A fast and accurate adapter trimmer for paired-end reads.
tags: [skewer, qc]
author: oxo-call-community
source_url: "https://github.com/relipmoc/skewer.git"
---

## Concepts

- **Tool Overview**: skewer (v0.2.2) - A fast and accurate adapter trimmer for paired-end reads.
- **Core Function**: A fast and accurate adapter trimmer for paired-end reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda skewer`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `skewer -i <input.fastq> -o <output_dir>`
**Explanation:** Run skewer with typical input and output options.
