---
name: consan
category: alignment
description: Pairwise RNA structural alignment, both unconstrained and constrained on alignment pins.
tags: [consan, alignment]
author: oxo-call-community
source_url: "http://eddylab.org/software/consan/README"
---

## Concepts

- **Tool Overview**: consan (v1.2) - Pairwise RNA structural alignment, both unconstrained and constrained on alignment pins.
- **Core Function**: Pairwise RNA structural alignment, both unconstrained and constrained on alignment pins.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda consan`

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
