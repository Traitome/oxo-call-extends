---
name: ditasic
category: metagenomics
description: DiTASiC - Abundance estimation and differential abundance assessment of taxa in metagenomics.
tags: [ditasic, metagenomics, abundance, differential, taxa]
author: oxo-call-community
source_url: "https://rki_bioinformatics.gitlab.io/ditasic/"
---

## Concepts

- **Tool Overview**: DiTASiC v0.2 - Comprehensive approach for abundance estimation and differential analysis in metagenomics.
- **Core Function**: Estimates taxon abundances and performs differential abundance testing between samples.
- **Input/Output**: Expects mapped reads and reference genomes; outputs abundance estimates and differential results.
- **Installation**: `conda install -c bioconda ditasic`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires read mappings and reference database.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `ditasic --mappings sample1.bam sample2.bam --reference refs.fa --output abundances.tsv`
**Explanation:** Estimates taxon abundances from metagenomic data.
