---
name: amap
category: alignment
description: AMAP is a multiple sequence alignment program based on sequence annealing.
tags: [amap, alignment]
author: oxo-call-community
source_url: "https://web.archive.org/web/20060902044446/http://bio.math.berkeley.edu/amap/"
---

## Concepts

- **Tool Overview**: amap (v2.2) - AMAP is a multiple sequence alignment program based on sequence annealing.
- **Core Function**: AMAP is a multiple sequence alignment program based on sequence annealing.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda amap`

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
