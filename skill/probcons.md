---
name: probcons
category: alignment
description: PROBCONS is a probabilistic consistency-based multiple sequence alignment
tags: ["probcons", "alignment"]
author: oxo-call-community
source_url: "http://probcons.stanford.edu/"
---

## Concepts

- **Tool Overview**: PROBCONS is a probabilistic consistency-based multiple sequence alignment (version 1.12)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda probcons`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

