---
name: rosella
category: alignment
description: Metagenomic binning pipeline and algorithm using UMAP and HDBSCAN
tags: ["rosella", "alignment"]
author: oxo-call-community
source_url: "https://github.com/rhysnewell/rosella.git"
---

## Concepts

- **Tool Overview**: Metagenomic binning pipeline and algorithm using UMAP and HDBSCAN (version 0.5.7)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rosella`

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

