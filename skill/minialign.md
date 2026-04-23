---
name: minialign
category: alignment
description: Fast and accurate alignment tool for PacBio and Nanopore long reads.
tags: [minialign, alignment]
author: oxo-call-community
source_url: "https://github.com/ocxtal/minialign"
---

## Concepts

- **Tool Overview**: minialign v0.6.0 - Minialign is a little bit fast and moderately accurate nucleotide sequence alignment tool designed for PacBio and Nanopore long reads. It is built on three key algorithms, minimizer-based index of the minimap overlapper, array-based seed chaining, and SIMD-parallel Smith-Waterman-Gotoh extension..
- **Core Function**: Fast and accurate alignment tool for PacBio and Nanopore long reads.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda minialign`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
