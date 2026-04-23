---
name: recmpox
category: alignment
description: RecMpox flags potential recombination events in monkeypox consensus genomes.
tags: ["recmpox", "alignment"]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/RecMpox/blob/main/README.md"
---

## Concepts

- **Tool Overview**: RecMpox flags potential recombination events in monkeypox consensus genomes. (version 0.0.5)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda recmpox`

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

