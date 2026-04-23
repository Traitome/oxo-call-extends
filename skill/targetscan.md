---
name: targetscan
category: annotation
description: Search for predicted microRNA targets in mammals
tags: [targetscan, annotation]
author: oxo-call-community
source_url: "https://www.targetscan.org/vert_80/"
---

## Concepts

- **Tool Overview**: targetscan (v7.0) - Search for predicted microRNA targets in mammals
- **Core Function**: Search for predicted microRNA targets in mammals
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda targetscan`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `targetscan -i <input.fasta> -o <output.gff>`
**Explanation:** Run targetscan with typical input and output options.
