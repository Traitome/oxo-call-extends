---
name: superstr
category: alignment
description: A lightweight, alignment-free utility for detecting repeat-containing reads in short-read WGS, WES and RNA-seq data.
tags: [superstr, alignment]
author: oxo-call-community
source_url: "https://github.com/bahlolab/superSTR"
---

## Concepts

- **Tool Overview**: superstr (v1.0.1) - A lightweight, alignment-free utility for detecting repeat-containing reads in short-read WGS, WES and RNA-seq data.
- **Core Function**: A lightweight, alignment-free utility for detecting repeat-containing reads in short-read WGS, WES and RNA-seq data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda superstr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `superstr -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run superstr with typical input and output options.
