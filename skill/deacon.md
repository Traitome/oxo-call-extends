---
name: deacon
category: alignment
description: Fast alignment-free sequence filter
tags: [deacon, alignment]
author: oxo-call-community
source_url: "https://github.com/bede/deacon"
---

## Concepts

- **Tool Overview**: deacon (v0.15.0) - Fast alignment-free sequence filter
- **Core Function**: Fast alignment-free sequence filter
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda deacon`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
