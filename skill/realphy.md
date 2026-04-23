---
name: realphy
category: alignment
description: The Reference sequence Alignment based Phylogeny
tags: ["realphy", "alignment"]
author: oxo-call-community
source_url: "https://realphy.unibas.ch/realphy"
---

## Concepts

- **Tool Overview**: The Reference sequence Alignment based Phylogeny (version 1.13)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda realphy`

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

