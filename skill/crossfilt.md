---
name: crossfilt
category: alignment
description: Tools to filter reads causing alignment bias in cross-species genomic comparisons.
tags: [crossfilt, alignment]
author: oxo-call-community
source_url: "https://github.com/kennethabarr/CrossFilt"
---

## Concepts

- **Tool Overview**: crossfilt (v0.2.1) - Tools to filter reads causing alignment bias in cross-species genomic comparisons.
- **Core Function**: Tools to filter reads causing alignment bias in cross-species genomic comparisons.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda crossfilt`

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
