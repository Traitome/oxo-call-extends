---
name: scte
category: alignment
description: scTE builds genome indices for the fast alignment of reads to genes and TEs.
tags: [scte, alignment]
author: oxo-call-community
source_url: "https://github.com/JiekaiLab/scTE"
---

## Concepts

- **Tool Overview**: scte (v1.0.0) - scTE builds genome indices for the fast alignment of reads to genes and TEs.
- **Core Function**: scTE builds genome indices for the fast alignment of reads to genes and TEs.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scte`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scte -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run scte with typical input and output options.
