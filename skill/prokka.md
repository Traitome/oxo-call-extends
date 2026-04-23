---
name: prokka
category: annotation
description: Rapid annotation of prokaryotic genomes
tags: ["prokka", "annotation"]
author: oxo-call-community
source_url: "https://github.com/tseemann/prokka"
---

## Concepts

- **Tool Overview**: Rapid annotation of prokaryotic genomes (version 1.15.6)
- **Core Function**: Processes bioinformatics data related to annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda prokka`

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

