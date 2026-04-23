---
name: shape_it
category: alignment
description: Shape alignment against a database of molecules
tags: [shape_it, alignment]
author: oxo-call-community
source_url: "http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/software/shape-it/1.0.1/shape-it.html"
---

## Concepts

- **Tool Overview**: shape_it (v1.0.1) - Shape alignment against a database of molecules
- **Core Function**: Shape alignment against a database of molecules
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shape_it`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shape_it -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run shape_it with typical input and output options.
