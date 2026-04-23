---
name: tassel
category: population-genomics
description: TASSEL is a software package to evaluate traits associations, evolutionary patterns, and linkage disequilibrium.
tags: [tassel, population-genomics]
author: oxo-call-community
source_url: "https://www.maizegenetics.net/tassel"
---

## Concepts

- **Tool Overview**: tassel (v5.2.89) - TASSEL is a software package to evaluate traits associations, evolutionary patterns, and linkage disequilibrium.
- **Core Function**: TASSEL is a software package to evaluate traits associations, evolutionary patterns, and linkage disequilibrium.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tassel`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tassel -i <input.vcf> -o <output_dir>`
**Explanation:** Run tassel with typical input and output options.
