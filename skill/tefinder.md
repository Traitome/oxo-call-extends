---
name: tefinder
category: annotation
description: Programs for transposable element search and annotation in large eukaryotic genome sequence.
tags: [tefinder, annotation]
author: oxo-call-community
source_url: "https://forge.inrae.fr/urgi/urgi-anagen/te_finder/-/blob/release-2.32/README.md"
---

## Concepts

- **Tool Overview**: tefinder (v2.32) - Programs for transposable element search and annotation in large eukaryotic genome sequence.
- **Core Function**: Programs for transposable element search and annotation in large eukaryotic genome sequence.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tefinder`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tefinder -i <input.fasta> -o <output.gff>`
**Explanation:** Run tefinder with typical input and output options.
