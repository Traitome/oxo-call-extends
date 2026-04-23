---
name: distle
category: population-genomics
description: Fast distance matrix calculations on FASTA and cgMLST files.
tags: [distle, population-genomics, distance-matrix, cgmlst]
author: oxo-call-community
source_url: "https://github.com/KHajji/distle"
---

## Concepts

- **Tool Overview**: distle v0.3.0 - Fast distance matrix calculation tool for FASTA and cgMLST files.
- **Core Function**: Computes pairwise distances between sequences or cgMLST profiles efficiently.
- **Input/Output**: Expects FASTA or cgMLST files; outputs distance matrices.
- **Installation**: `conda install -c bioconda distle`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FASTA or cgMLST allele profiles.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `distle --input profiles.tsv --output distances.tsv`
**Explanation:** Calculates distance matrix from profiles.
