---
name: tepeaks
category: epigenomics
description: Package for including repetitive regions in peak calling from ChIP-seq datasets.
tags: [tepeaks, epigenomics]
author: oxo-call-community
source_url: "http://hammelllab.labsites.cshl.edu/software/#TEpeaks"
---

## Concepts

- **Tool Overview**: tepeaks (v0.1) - Package for including repetitive regions in peak calling from ChIP-seq datasets.
- **Core Function**: Package for including repetitive regions in peak calling from ChIP-seq datasets.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tepeaks`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tepeaks -i <input.bam> -o <output_dir>`
**Explanation:** Run tepeaks with typical input and output options.
