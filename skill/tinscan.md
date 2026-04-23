---
name: tinscan
category: alignment
description: Find alignment signatures characteristic of transposon insertion sites.
tags: [tinscan, alignment]
author: oxo-call-community
source_url: "https://github.com/Adamtaranto/TE-insertion-scanner/blob/0.2.1/README.md"
---

## Concepts

- **Tool Overview**: tinscan (v0.2.1) - Find alignment signatures characteristic of transposon insertion sites.
- **Core Function**: Find alignment signatures characteristic of transposon insertion sites.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tinscan`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tinscan -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run tinscan with typical input and output options.
