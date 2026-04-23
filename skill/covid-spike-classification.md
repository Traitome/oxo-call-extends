---
name: covid-spike-classification
category: variant-calling
description: Detect interesting SARS-CoV-2 spike protein variants from Sanger sequencing data.
tags: [covid-spike-classification, variant-calling]
author: oxo-call-community
source_url: "https://github.com/kblin/covid-spike-classification/"
---

## Concepts

- **Tool Overview**: covid-spike-classification (v0.6.4) - Detect interesting SARS-CoV-2 spike protein variants from Sanger sequencing data.
- **Core Function**: Detect interesting SARS-CoV-2 spike protein variants from Sanger sequencing data.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda covid-spike-classification`

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
