---
name: conga
category: variant-calling
description: Copy number variation genotyping in ancient genomes and low-coverage sequencing data.
tags: [conga, variant-calling]
author: oxo-call-community
source_url: "https://github.com/asylvz/CONGA"
---

## Concepts

- **Tool Overview**: conga (v1.1) - Copy number variation genotyping in ancient genomes and low-coverage sequencing data.
- **Core Function**: Copy number variation genotyping in ancient genomes and low-coverage sequencing data.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda conga`

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
