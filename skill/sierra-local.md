---
name: sierra-local
category: annotation
description: sierra-local is a Python3 implementation of the Stanford HIVdb Sierra service for generating drug resistance predictions from HIV-1 sequences.
tags: [sierra-local, annotation]
author: oxo-call-community
source_url: "https://github.com/PoonLab/sierra-local"
---

## Concepts

- **Tool Overview**: sierra-local (v0.4.4) - sierra-local is a Python3 implementation of the Stanford HIVdb Sierra service for generating drug resistance predictions from HIV-1 sequences.
- **Core Function**: sierra-local is a Python3 implementation of the Stanford HIVdb Sierra service for generating drug resistance predictions from HIV-1 sequences.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sierra-local`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sierra-local -i <input.fasta> -o <output.gff>`
**Explanation:** Run sierra-local with typical input and output options.
