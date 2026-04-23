---
name: trand
category: expression
description: transcript event and distance
tags: [trand, expression]
author: oxo-call-community
source_url: "https://github.com/McIntyre-Lab/TranD"
---

## Concepts

- **Tool Overview**: trand (v22.10.13) - TranD is a collection of tools to facilitate metrics of structural variation for whole genome transcript annotation files (GTF) that pinpoint structural variation to the nucleotide level.
- **Core Function**: transcript event and distance
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda trand`

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
