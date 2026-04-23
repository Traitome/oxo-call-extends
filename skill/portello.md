---
name: portello
category: alignment
description: Transfer HiFi read mappings from their own assembly contigs to a standard reference
tags: ["portello", "alignment"]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/portello"
---

## Concepts

- **Tool Overview**: Transfer HiFi read mappings from their own assembly contigs to a standard reference (version 0.7.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda portello`

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

