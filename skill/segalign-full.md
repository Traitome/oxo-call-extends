---
name: segalign-full
category: alignment
description: SegAlign: A Scalable GPU-Based Whole Genome Aligner
tags: [segalign-full, alignment]
author: oxo-call-community
source_url: "https://github.com/galaxyproject/SegAlign/blob/main/README.md"
---

## Concepts

- **Tool Overview**: segalign-full (v0.1.2.7) - SegAlign: A Scalable GPU-Based Whole Genome Aligner
- **Core Function**: SegAlign: A Scalable GPU-Based Whole Genome Aligner
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda segalign-full`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `segalign-full -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run segalign-full with typical input and output options.
