---
name: rasusa
category: alignment
description: Randomly subsample sequencing reads or alignments
tags: ["rasusa", "alignment", "sam"]
author: oxo-call-community
source_url: "https://github.com/mbhall88/rasusa"
---

## Concepts

- **Tool Overview**: Randomly subsample sequencing reads or alignments (version 4.0.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rasusa`

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

