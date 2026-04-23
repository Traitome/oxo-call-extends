---
name: atac
category: alignment
description: ATAC is a computational process for comparative mapping between two genome assemblies, or between two different genomes.
tags: [atac, alignment]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/kmer"
---

## Concepts

- **Tool Overview**: atac (v2008) - ATAC is a computational process for comparative mapping between two genome assemblies, or between two different genomes.
- **Core Function**: ATAC is a computational process for comparative mapping between two genome assemblies, or between two different genomes.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda atac`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
