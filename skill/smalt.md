---
name: smalt
category: alignment
description: SMALT aligns DNA sequencing reads with a reference genome.
tags: [smalt, alignment]
author: oxo-call-community
source_url: "https://www.sanger.ac.uk/tool/smalt"
---

## Concepts

- **Tool Overview**: smalt (v0.7.6) - SMALT aligns DNA sequencing reads with a reference genome.
- **Core Function**: SMALT aligns DNA sequencing reads with a reference genome.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smalt`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smalt -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run smalt with typical input and output options.
