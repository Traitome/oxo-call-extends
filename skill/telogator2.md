---
name: telogator2
category: utility
description: Analyze allele-specific telomere length from PacBio and Nanopore reads
tags: [telogator2, utility]
author: oxo-call-community
source_url: "https://github.com/zstephens/telogator2/blob/main/README.md"
---

## Concepts

- **Tool Overview**: telogator2 (v2.2.3) - Analyze allele-specific telomere length from PacBio and Nanopore reads
- **Core Function**: Analyze allele-specific telomere length from PacBio and Nanopore reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda telogator2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `telogator2 -i <input_file> -o <output_file>`
**Explanation:** Run telogator2 with typical input and output options.
