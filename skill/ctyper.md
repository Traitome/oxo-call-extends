---
name: ctyper
category: variant-calling
description: Genotyping sequence-resolved copy-number variation using pangenomes.
tags: [ctyper, variant-calling]
author: oxo-call-community
source_url: "https://github.com/ChaissonLab/Ctyper"
---

## Concepts

- **Tool Overview**: ctyper (v1.0.5) - Genotyping sequence-resolved copy-number variation using pangenomes.
- **Core Function**: Genotyping sequence-resolved copy-number variation using pangenomes.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ctyper`

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
