---
name: alv
category: alignment
description: A console-based sequence alignment viewer
tags: [alv, alignment]
author: oxo-call-community
source_url: "https://github.com/arvestad/alv"
---

## Concepts

- **Tool Overview**: alv (v1.8.2) - A console-based sequence alignment viewer
- **Core Function**: A console-based sequence alignment viewer
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda alv`

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
