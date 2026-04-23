---
name: swalign
category: alignment
description: Smith-Waterman local aligner
tags: [swalign, alignment]
author: oxo-call-community
source_url: "https://github.com/mbreese/swalign/"
---

## Concepts

- **Tool Overview**: swalign (v0.3.7) - Smith-Waterman local aligner
- **Core Function**: Smith-Waterman local aligner
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda swalign`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `swalign -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run swalign with typical input and output options.
