---
name: cats-rf
category: expression
description: Reference-free transcriptome assembly quality assessment tool.
tags: [cats-rf, expression]
author: oxo-call-community
source_url: "https://github.com/bodulic/CATS-rf/blob/main/README.md"
---

## Concepts

- **Tool Overview**: cats-rf (v1.0.4) - Reference-free transcriptome assembly quality assessment tool.
- **Core Function**: CATS-rf evaluates transcriptome assemblies using RNA-seq reads without requiring a reference genome.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cats-rf`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
