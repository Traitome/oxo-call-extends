---
name: dgenies
category: utility
description: Dotplot large Genomes in an Interactive, Efficient and Simple way.
tags: [dgenies, utility, dotplot, visualization, genome-comparison]
author: oxo-call-community
source_url: "http://dgenies.toulouse.inrae.fr"
---

## Concepts

- **Tool Overview**: D-Genies v1.5.0 - Interactive tool for generating dot plots of large genome alignments.
- **Core Function**: Creates interactive dot plots for visualizing genome-to-genome alignments and synteny.
- **Input/Output**: Expects FASTA files or alignment results; outputs interactive dot plot visualizations.
- **Installation**: `conda install -c bioconda dgenies`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires genome FASTA or pre-computed alignment files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dgenies --target genome1.fa --query genome2.fa --output dotplot/`
**Explanation:** Generates interactive dot plot comparing two genomes.
