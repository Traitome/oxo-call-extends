---
name: alnstats
category: alignment
description: A high-performance command-line tool designed to calculate yield and duplicate statistics from BAM, SAM, or CRAM alignment files
tags: [alnstats, alignment, BAM, SAM, CRAM]
author: oxo-call-community
source_url: "https://github.com/Poshi/alnstats"
---

## Concepts

- **Tool Overview**: alnstats (v0.1.1) - A high-performance command-line tool designed to calculate yield and duplicate statistics from BAM, SAM, or CRAM alignment files
- **Core Function**: A high-performance command-line tool designed to calculate yield and duplicate statistics from BAM, SAM, or CRAM alignment files
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda alnstats`

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
