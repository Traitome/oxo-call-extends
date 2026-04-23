---
name: squizz
category: alignment
description: Squizz is a sequence/alignment format checker, but it has some conversion capabilities too.
tags: [squizz, alignment]
author: oxo-call-community
source_url: "http://ftp.pasteur.fr/pub/gensoft/projects/squizz/"
---

## Concepts

- **Tool Overview**: squizz (v0.99d) - Squizz is a sequence/alignment format checker, but it has some conversion capabilities too.
- **Core Function**: Squizz is a sequence/alignment format checker, but it has some conversion capabilities too.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda squizz`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `squizz -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run squizz with typical input and output options.
