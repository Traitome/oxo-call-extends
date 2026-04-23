---
name: cesar
category: alignment
description: CESAR 2.0 is a method to realign coding exons or genes to DNA sequences using a Hidden Markov Model.
tags: [cesar, alignment]
author: oxo-call-community
source_url: "https://github.com/hillerlab/CESAR2.0"
---

## Concepts

- **Tool Overview**: cesar (v1.02) - CESAR 2.0 is a method to realign coding exons or genes to DNA sequences using a Hidden Markov Model.
- **Core Function**: CESAR 2.0 is a method to realign coding exons or genes to DNA sequences using a Hidden Markov Model.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cesar`

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
