---
name: snippy
category: alignment
description: Rapid bacterial SNP calling and core genome alignments
tags: [snippy, alignment]
author: oxo-call-community
source_url: "https://github.com/tseemann/snippy"
---

## Concepts

- **Tool Overview**: snippy (v4.6.0) - Rapid bacterial SNP calling and core genome alignments
- **Core Function**: Rapid bacterial SNP calling and core genome alignments
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snippy`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snippy -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run snippy with typical input and output options.
