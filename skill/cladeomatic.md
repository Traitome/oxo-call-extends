---
name: cladeomatic
category: variant-calling
description: Clade-O-Matic: Automatic recognition of population structures based on canonical SNPs
tags: [cladeomatic, variant-calling]
author: oxo-call-community
source_url: "https://github.com/phac-nml/cladeomatic"
---

## Concepts

- **Tool Overview**: cladeomatic (v0.1.1) - Clade-O-Matic: Automatic recognition of population structures based on canonical SNPs
- **Core Function**: Clade-O-Matic: Automatic recognition of population structures based on canonical SNPs
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cladeomatic`

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
