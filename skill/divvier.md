---
name: divvier
category: alignment
description: A program for removing multiple sequence alignment uncertainty.
tags: [divvier, alignment, uncertainty, trimming]
author: oxo-call-community
source_url: "https://github.com/simonwhelan/Divvier"
---

## Concepts

- **Tool Overview**: Divvier v1.01 - Tool for removing uncertain regions from multiple sequence alignments.
- **Core Function**: Identifies and removes alignment columns with high uncertainty or ambiguity.
- **Input/Output**: Expects multiple sequence alignments; outputs cleaned alignments with reduced uncertainty.
- **Installation**: `conda install -c bioconda divvier`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires multiple sequence alignment in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `divvier --input alignment.fa --output cleaned.fa`
**Explanation:** Removes uncertain regions from alignment.
