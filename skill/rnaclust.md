---
name: rnaclust
category: alignment
description: A tool for clustering of RNAs based on their secondary structures using LocARNA
tags: ["rnaclust", "alignment", "fasta"]
author: oxo-call-community
source_url: "http://www.bioinf.uni-leipzig.de/~kristin/Software/RNAclust/"
---

## Concepts

- **Tool Overview**: A tool for clustering of RNAs based on their secondary structures using LocARNA (version 1.3)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rnaclust`

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

