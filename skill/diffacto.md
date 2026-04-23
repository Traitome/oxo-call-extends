---
name: diffacto
category: annotation
description: A protein summarization method for shotgun proteomics experiments.
tags: [diffacto, annotation, proteomics, protein-summarization, quantification]
author: oxo-call-community
source_url: "https://github.com/statisticalbiotechnology/diffacto"
---

## Concepts

- **Tool Overview**: Diffacto v1.0.7 - Protein summarization method for shotgun proteomics that combines peptide-level quantifications.
- **Core Function**: Summarizes peptide-level quantifications to protein-level abundances with quality weights.
- **Input/Output**: Expects peptide quantification tables; outputs protein-level summaries with confidence scores.
- **Installation**: `conda install -c bioconda diffacto`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires peptide-level quantification data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `diffacto --input peptides.tsv --output proteins.tsv`
**Explanation:** Summarizes peptide quantifications to protein level.
