---
name: prank
category: alignment
description: PRANK is a probabilistic multiple alignment program for DNA, codon and amino-acid sequences.
tags: ["prank", "alignment"]
author: oxo-call-community
source_url: "https://ariloytynoja.github.io/prank-msa"
---

## Concepts

- **Tool Overview**: PRANK is a probabilistic multiple alignment program for DNA, codon and amino-acid sequences. (version 251117)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda prank`

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

