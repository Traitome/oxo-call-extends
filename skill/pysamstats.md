---
name: pysamstats
category: alignment
description: Calculate read mapping stats from SAM/BAM/CRAM
tags: ["pysamstats", "alignment", "bam", "sam", "bam"]
author: oxo-call-community
source_url: "https://github.com/alimanfoo/pysamstats"
---

## Concepts

- **Tool Overview**: Calculate read mapping stats from SAM/BAM/CRAM (version 1.1.2)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pysamstats`

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

