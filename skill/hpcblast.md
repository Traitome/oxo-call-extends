---
name: hpcblast
category: hpc
description: A wrapper for NCBI-BLAST+ suite which provides a simple and efficient method to accelerate the blast search
tags: [hpcblast, hpc]
author: oxo-call-community
source_url: "https://github.com/yodeng/hpc-blast"
---

## Concepts

- **Tool Overview**: hpcblast (v1.0.2) - A wrapper for NCBI-BLAST+ suite which provides a simple and efficient method to accelerate the blast search
- **Core Function**: Provides functionality for hpc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hpcblast`

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
