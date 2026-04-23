---
name: hera
category: alignment
description: hera is a bioinformatics tool that helps analyze RNA-seq data, providing base-to-base alignment BAM files, transcript abundance estimation, and fusion gene detection.
tags: [hera, alignment, BAM]
author: oxo-call-community
source_url: "https://github.com/bioturing/hera"
---

## Concepts

- **Tool Overview**: hera (v1.1) - hera is a bioinformatics tool that helps analyze RNA-seq data, providing base-to-base alignment BAM files, transcript abundance estimation, and fusion gene detection.
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hera`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
