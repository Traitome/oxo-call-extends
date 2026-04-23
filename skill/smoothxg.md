---
name: smoothxg
category: alignment
description: Local reconstruction of variation graphs using partial order alignment.
tags: [smoothxg, alignment]
author: oxo-call-community
source_url: "https://github.com/pangenome/smoothxg/blob/v0.8.2/README.md"
---

## Concepts

- **Tool Overview**: smoothxg (v0.8.2) - Local reconstruction of variation graphs using partial order alignment.
- **Core Function**: Local reconstruction of variation graphs using partial order alignment.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smoothxg`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smoothxg -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run smoothxg with typical input and output options.
