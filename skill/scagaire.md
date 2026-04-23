---
name: scagaire
category: annotation
description: Scagaire allows you to take in gene predictions from a metagenomic sample and filter them by bacterial/pathogenic species
tags: ["scagaire", "annotation", "sam"]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/scagaire"
---

## Concepts

- **Tool Overview**: Scagaire allows you to take in gene predictions from a metagenomic sample and filter them by bacterial/pathogenic species (version 0.0.4)
- **Core Function**: Processes bioinformatics data related to annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda scagaire`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Annotate features
**Args:** `-i genome.fasta -o annotation.gff`
**Explanation:** Predicts and annotates genomic features.

