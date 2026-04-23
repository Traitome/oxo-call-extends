---
name: pseudo-it
category: alignment
description: Reference-based genome assembly with iterative mapping
tags: ["pseudo-it", "alignment"]
author: oxo-call-community
source_url: "https://github.com/goodest-goodlab/pseudo-it"
---

## Concepts

- **Tool Overview**: Reference-based genome assembly with iterative mapping (version 3.1.1)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pseudo-it`

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

