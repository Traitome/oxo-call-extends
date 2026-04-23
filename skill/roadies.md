---
name: roadies
category: alignment
description: Reference-free Orthology-free Alignment-free DIscordance aware Estimation of Species tree (ROADIES).
tags: ["roadies", "alignment"]
author: oxo-call-community
source_url: "https://turakhia.ucsd.edu/ROADIES"
---

## Concepts

- **Tool Overview**: Reference-free Orthology-free Alignment-free DIscordance aware Estimation of Species tree (ROADIES). (version 0.1.10)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda roadies`

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

