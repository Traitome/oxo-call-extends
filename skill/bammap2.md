---
name: bammap2
category: alignment
description: A fast BAM file mapping tool
tags: [bammap2, alignment, BAM]
author: oxo-call-community
source_url: "https://github.com/wangyibin/bammap2"
---

## Concepts

- **Tool Overview**: bammap2 (v0.1.7) - A fast BAM file mapping tool
- **Core Function**: A fast BAM file mapping tool
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda bammap2`

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
