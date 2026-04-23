---
name: control-freec
category: variant-calling
description: Copy number and genotype annotation from whole genome and whole exome sequencing data.
tags: [control-freec, variant-calling]
author: oxo-call-community
source_url: "https://github.com/BoevaLab/FREEC"
---

## Concepts

- **Tool Overview**: control-freec (v11.6) - Copy number and genotype annotation from whole genome and whole exome sequencing data.
- **Core Function**: Copy number and genotype annotation from whole genome and whole exome sequencing data.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda control-freec`

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
