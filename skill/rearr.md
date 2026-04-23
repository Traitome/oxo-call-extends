---
name: rearr
category: alignment
description: Chimeric alignment of CRISPR-seq
tags: ["rearr", "alignment"]
author: oxo-call-community
source_url: "https://ljw20180420.github.io/rearr"
---

## Concepts

- **Tool Overview**: Chimeric alignment of CRISPR-seq (version 1.0.15)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rearr`

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

