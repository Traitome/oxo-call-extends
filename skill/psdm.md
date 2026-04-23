---
name: psdm
category: alignment
description: Compute a pairwise SNP distance matrix from one or two alignment(s)
tags: ["psdm", "alignment"]
author: oxo-call-community
source_url: "https://github.com/mbhall88/psdm"
---

## Concepts

- **Tool Overview**: Compute a pairwise SNP distance matrix from one or two alignment(s) (version 0.3.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda psdm`

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

