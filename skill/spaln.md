---
name: spaln
category: alignment
description: Map and align a set of cDNA/EST or protein sequences onto a genome.
tags: [spaln, alignment]
author: oxo-call-community
source_url: "https://github.com/ogotoh/spaln/blob/ver.3.0.8/README.md"
---

## Concepts

- **Tool Overview**: spaln (v3.0.8) - Map and align a set of cDNA/EST or protein sequences onto a genome.
- **Core Function**: Map and align a set of cDNA/EST or protein sequences onto a genome.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spaln`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spaln -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run spaln with typical input and output options.
