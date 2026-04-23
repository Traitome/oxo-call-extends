---
name: strmie-hd
category: annotation
description: Automated Huntington Disease polyQ pattern scanner.
tags: [strmie-hd, annotation]
author: oxo-call-community
source_url: "https://mazzalab.github.io/STRmie-HD/"
---

## Concepts

- **Tool Overview**: strmie-hd (v1.0.0) - Automated Huntington Disease polyQ pattern scanner.
- **Core Function**: Automated Huntington Disease polyQ pattern scanner.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda strmie-hd`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `strmie-hd -i <input.fasta> -o <output.gff>`
**Explanation:** Run strmie-hd with typical input and output options.
