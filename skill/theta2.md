---
name: theta2
category: utility
description: Estimate tumor purity and clonal/subclonal copy number aberrations directly from high-throughput DNA sequencing data
tags: [theta2, utility]
author: oxo-call-community
source_url: "https://github.com/raphael-group/THetA"
---

## Concepts

- **Tool Overview**: theta2 (v0.7) - Estimate tumor purity and clonal/subclonal copy number aberrations directly from high-throughput DNA sequencing data
- **Core Function**: Estimate tumor purity and clonal/subclonal copy number aberrations directly from high-throughput DNA sequencing data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda theta2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `theta2 -i <input_file> -o <output_file>`
**Explanation:** Run theta2 with typical input and output options.
