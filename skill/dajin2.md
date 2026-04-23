---
name: dajin2
category: variant-calling
description: One-step genotyping tools for targeted long-read sequencing.
tags: [dajin2, variant-calling]
author: oxo-call-community
source_url: "https://github.com/akikuno/DAJIN2/blob/0.9.2/README.md"
---

## Concepts

- **Tool Overview**: dajin2 (v0.9.2) - One-step genotyping tools for targeted long-read sequencing.
- **Core Function**: One-step genotyping tools for targeted long-read sequencing.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda dajin2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
