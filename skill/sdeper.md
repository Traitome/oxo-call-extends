---
name: sdeper
category: expression
description: Spatial Deconvolution method with Platform Effect Removal
tags: [sdeper, expression]
author: oxo-call-community
source_url: "https://sdeper.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: sdeper (v2.0.0) - Spatial Deconvolution method with Platform Effect Removal
- **Core Function**: Spatial Deconvolution method with Platform Effect Removal
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sdeper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sdeper -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run sdeper with typical input and output options.
