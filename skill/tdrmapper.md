---
name: tdrmapper
category: alignment
description: tRNA detection and quantification
tags: [tdrmapper, alignment]
author: oxo-call-community
source_url: "https://github.com/sararselitsky/tDRmapper"
---

## Concepts

- **Tool Overview**: tdrmapper (v1.1) - tRNA detection and quantification
- **Core Function**: tRNA detection and quantification
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tdrmapper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tdrmapper -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run tdrmapper with typical input and output options.
