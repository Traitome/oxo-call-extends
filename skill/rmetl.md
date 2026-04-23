---
name: rmetl
category: alignment
description: rMETL is a realignment-based Mobile Element insertion detection Tool for Long read
tags: ["rmetl", "alignment"]
author: oxo-call-community
source_url: "https://github.com/tjiangHIT/rMETL"
---

## Concepts

- **Tool Overview**: rMETL is a realignment-based Mobile Element insertion detection Tool for Long read (version 1.0.4)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rmetl`

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

