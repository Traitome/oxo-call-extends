---
name: rnaframework
category: alignment
description: Toolkit for the analysis of RNA structures and post-transcriptional modifications from HTS data
tags: ["rnaframework", "alignment"]
author: oxo-call-community
source_url: "https://rnaframework-docs.readthedocs.io/"
---

## Concepts

- **Tool Overview**: Toolkit for the analysis of RNA structures and post-transcriptional modifications from HTS data (version 2.9.6)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rnaframework`

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

