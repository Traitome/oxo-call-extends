---
name: snpomatic
category: alignment
description: SNP-o-matic is a fast, stringent short-read mapping software.
tags: [snpomatic, alignment]
author: oxo-call-community
source_url: "https://github.com/magnusmanske/snpomatic"
---

## Concepts

- **Tool Overview**: snpomatic (v1.0) - SNP-o-matic is a fast, stringent short-read mapping software.
- **Core Function**: SNP-o-matic is a fast, stringent short-read mapping software.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snpomatic`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snpomatic -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run snpomatic with typical input and output options.
