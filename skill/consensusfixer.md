---
name: consensusfixer
category: alignment
description: Computes a consensus sequence with wobbles, ambiguous bases, and in-frame insertions, from a NGS read alignment.
tags: [consensusfixer, alignment]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/ConsensusFixer"
---

## Concepts

- **Tool Overview**: consensusfixer (v0.4) - Computes a consensus sequence with wobbles, ambiguous bases, and in-frame insertions, from a NGS read alignment.
- **Core Function**: Computes a consensus sequence with wobbles, ambiguous bases, and in-frame insertions, from a NGS read alignment.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda consensusfixer`

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
