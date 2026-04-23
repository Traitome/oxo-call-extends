---
name: clumppling
category: alignment
description: Cluster matching and permutation program with integer linear programming.
tags: [clumppling, alignment]
author: oxo-call-community
source_url: "https://github.com/PopGenClustering/Clumppling/blob/master/Clumppling_Manual.pdf"
---

## Concepts

- **Tool Overview**: clumppling (v2.0.7) - Cluster matching and permutation program with integer linear programming.
- **Core Function**: Clumppling (CLUster Matching and Permutation Program that uses integer Linear programmING) is a framework for aligning clustering results of population structure analysis.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda clumppling`

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
