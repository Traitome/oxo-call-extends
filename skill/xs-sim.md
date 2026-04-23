---
name: xs-sim
category: utility
description: Simulates NGS reads
tags: [xs-sim, utility, fastq]
author: oxo-call-community
source_url: "https://github.com/pratas/xs"
---

## Concepts

- **Tool Overview**: xs-sim (v2) - XS is a skilled FASTQ read simulation tool, flexible, portable (does not need a reference sequence) and tunable in terms of sequence complexity
- **Core Function**: Simulates NGS reads
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda xs-sim`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
