---
name: smithwaterman
category: alignment
description: Smith-waterman-gotoh alignment algorithm.
tags: [smithwaterman, alignment]
author: oxo-call-community
source_url: "https://github.com/ekg/smithwaterman"
---

## Concepts

- **Tool Overview**: smithwaterman (v1.0.0) - Smith-waterman-gotoh alignment algorithm.
- **Core Function**: Smith-waterman-gotoh alignment algorithm.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smithwaterman`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smithwaterman -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run smithwaterman with typical input and output options.
