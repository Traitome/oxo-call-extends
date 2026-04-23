---
name: samstats
category: alignment
description: SAM file alignment statistics at the read level
tags: ["samstats", "alignment", "sam"]
author: oxo-call-community
source_url: "https://github.com/kundajelab/SAMstats"
---

## Concepts

- **Tool Overview**: SAM file alignment statistics at the read level (version 0.2.2)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda samstats`

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

