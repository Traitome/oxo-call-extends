---
name: covar
category: variant-calling
description: Linked-read variant calling tool for wastewater sequencing data.
tags: [covar, variant-calling]
author: oxo-call-community
source_url: "https://github.com/andersen-lab/covar"
---

## Concepts

- **Tool Overview**: covar (v0.3.0) - Linked-read variant calling tool for wastewater sequencing data.
- **Core Function**: Linked-read variant calling tool for wastewater sequencing data.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda covar`

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
