---
name: svim-asm
category: alignment
description: SVIM-asm is a fork of the SV caller SVIM for genome-genome alignments.
tags: [svim-asm, alignment]
author: oxo-call-community
source_url: "https://github.com/eldariont/svim-asm"
---

## Concepts

- **Tool Overview**: svim-asm (v1.0.3) - SVIM-asm is a fork of the SV caller SVIM for genome-genome alignments.
- **Core Function**: SVIM-asm is a fork of the SV caller SVIM for genome-genome alignments.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svim-asm`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svim-asm -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run svim-asm with typical input and output options.
