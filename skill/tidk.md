---
name: tidk
category: annotation
description: Identify and find telomeres, or telomeric repeats in a genome.
tags: [tidk, annotation]
author: oxo-call-community
source_url: "https://github.com/tolkit/telomeric-identifier/blob/v0.2.7/README.md"
---

## Concepts

- **Tool Overview**: tidk (v0.2.65) - Identify and find telomeres, or telomeric repeats in a genome.
- **Core Function**: Identify and find telomeres, or telomeric repeats in a genome.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tidk`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tidk -i <input.fasta> -o <output.gff>`
**Explanation:** Run tidk with typical input and output options.
