---
name: daligner
category: alignment
description: DALIGNER: Find all significant local alignments between reads.
tags: [daligner, alignment]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/DALIGNER/blob/master/README.md"
---

## Concepts

- **Tool Overview**: daligner (v2.0.20240118) - DALIGNER: Find all significant local alignments between reads.
- **Core Function**: DALIGNER: Find all significant local alignments between reads.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda daligner`

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
