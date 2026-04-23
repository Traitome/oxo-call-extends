---
name: simo-omics
category: alignment
description: Spatial integration of multi-omics single-cell datasets through probabilistic alignment
tags: [simo-omics, alignment]
author: oxo-call-community
source_url: "https://github.com/ZJUFanLab/SIMO"
---

## Concepts

- **Tool Overview**: simo-omics (v1.0.0) - Spatial integration of multi-omics single-cell datasets through probabilistic alignment
- **Core Function**: Spatial integration of multi-omics single-cell datasets through probabilistic alignment
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda simo-omics`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `simo-omics -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run simo-omics with typical input and output options.
