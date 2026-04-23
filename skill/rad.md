---
name: rad
category: alignment
description: Read-structure Agnostic Demultiplexer for long-read single-cell RNA-seq.
tags: ["rad", "alignment", "csv"]
author: oxo-call-community
source_url: "https://github.com/indianewok/rad/blob/v0.6.0/README.md"
---

## Concepts

- **Tool Overview**: Read-structure Agnostic Demultiplexer for long-read single-cell RNA-seq. (version 0.6.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rad`

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

