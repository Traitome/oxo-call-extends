---
name: strobealign
category: alignment
description: Align short reads using dynamic seed size with strobemers
tags: [strobealign, alignment]
author: oxo-call-community
source_url: "https://github.com/ksahlin/strobealign"
---

## Concepts

- **Tool Overview**: strobealign (v0.17.0) - Align short reads using dynamic seed size with strobemers
- **Core Function**: Align short reads using dynamic seed size with strobemers
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strobealign`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strobealign -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run strobealign with typical input and output options.
