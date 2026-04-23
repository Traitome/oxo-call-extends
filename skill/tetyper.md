---
name: tetyper
category: annotation
description: Typing of a specific transposable element (TE) of interest from paired-end sequencing data.
tags: [tetyper, annotation]
author: oxo-call-community
source_url: "https://github.com/aesheppard/TETyper"
---

## Concepts

- **Tool Overview**: tetyper (v1.1) - Typing of a specific transposable element (TE) of interest from paired-end sequencing data.
- **Core Function**: Typing of a specific transposable element (TE) of interest from paired-end sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tetyper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tetyper -i <input.fasta> -o <output.gff>`
**Explanation:** Run tetyper with typical input and output options.
