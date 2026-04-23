---
name: metacluster
category: alignment
description: MetaCluster5.1 is a new software for binning short pair-end reads
tags: [metacluster, alignment, sequence, alignment]
author: oxo-call-community
source_url: "http://i.cs.hku.hk/~alse/MetaCluster/"
---

## Concepts

- **Tool Overview**: metacluster v5.1 - MetaCluster5.1 is an unsupervised binning method that can (1) samples with low-abundance species, or (2) samples (even with high-abundance) with many extremely-low-abundance species. The input file should be in fasta format. Every odd-number read and its next read are supposed to be pair-end reads..
- **Core Function**: MetaCluster5.1 is a new software for binning short pair-end reads
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda metacluster`

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
