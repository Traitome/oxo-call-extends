---
name: cellrank-krylov
category: alignment
description: CellRank for directed single-cell fate mapping
tags: [cellrank-krylov, alignment]
author: oxo-call-community
source_url: "https://cellrank.org"
---

## Concepts

- **Tool Overview**: cellrank-krylov (v1.5.1) - CellRank for directed single-cell fate mapping
- **Core Function**: CellRank is a toolkit to uncover cellular dynamics based on Markov state modeling of single-cell data. It contains two main modules: kernels compute cell-cell transition probabilities and estimators g...
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda cellrank-krylov`

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
