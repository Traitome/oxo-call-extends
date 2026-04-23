---
name: daisysuite
category: alignment
description: DaisySuite - mapping-based pipeline for horizontal gene transfer (HGT) detection using sequencing data
tags: [daisysuite, alignment]
author: oxo-call-community
source_url: "https://gitlab.com/eseiler/DaisySuite"
---

## Concepts

- **Tool Overview**: daisysuite (v1.3.0) - DaisySuite - mapping-based pipeline for horizontal gene transfer (HGT) detection using sequencing data
- **Core Function**: DaisySuite - mapping-based pipeline for horizontal gene transfer (HGT) detection using sequencing data
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda daisysuite`

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
