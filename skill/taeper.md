---
name: taeper
category: annotation
description: Simulate repeating a nanopore experiment.
tags: [taeper, annotation]
author: oxo-call-community
source_url: "https://github.com/mbhall88/taeper"
---

## Concepts

- **Tool Overview**: taeper (v0.1.0) - Simulate repeating a nanopore experiment.
- **Core Function**: Simulate repeating a nanopore experiment.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taeper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taeper -i <input.fasta> -o <output.gff>`
**Explanation:** Run taeper with typical input and output options.
