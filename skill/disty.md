---
name: disty
category: population-genomics
description: Disty McMatrixface - compute distance matrix from core genome alignment.
tags: [disty, population-genomics, distance-matrix, core-genome]
author: oxo-call-community
source_url: "https://github.com/c2-d2/disty"
---

## Concepts

- **Tool Overview**: disty v0.1.0 - Fast distance matrix computation from core genome alignments.
- **Core Function**: Calculates pairwise distances from core genome alignment files.
- **Input/Output**: Expects core genome alignment (FASTA); outputs distance matrix.
- **Installation**: `conda install -c bioconda disty`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires core genome multiple sequence alignment.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `disty --alignment core_aln.fa --output distances.tsv`
**Explanation:** Computes distance matrix from core genome alignment.
