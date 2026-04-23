---
name: cialign
category: alignment
description: Toolkit for cleaning and interpreting multiple sequence alignments
tags: [cialign, alignment]
author: oxo-call-community
source_url: "https://github.com/KatyBrown/CIAlign"
---

## Concepts

- **Tool Overview**: cialign (v1.1.4) - Toolkit for cleaning and interpreting multiple sequence alignments
- **Core Function**: Toolkit for cleaning and interpreting multiple sequence alignments
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cialign`

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
