---
name: musicc
category: metagenomics
description: MUSICC: A marker genes based framework for metagenomic normalization and accurate profiling of gene abundances in the microbiome.
tags: [musicc, metagenomics, normalization, marker-genes, microbiome]
author: oxo-call-community
source_url: "http://elbo.gs.washington.edu/software_musicc.html"
---

## Concepts

- **Tool Overview**: MUSiCC v1.0.4 - marker genes based framework for metagenomic normalization and gene abundance profiling.
- **Core Function**: Normalizes metagenomic gene abundance data using marker genes for accurate microbiome profiling.
- **Input/Output**: Takes gene abundance tables; outputs normalized abundance profiles.
- **Installation**: `conda install -c bioconda musicc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct gene abundance table format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i gene_abundances.tsv -o normalized.tsv`
**Explanation:** Normalizes gene abundance table using marker gene-based normalization.
