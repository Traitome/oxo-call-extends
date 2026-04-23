---
name: degenotate
category: population-genomics
description: Degeneracy annotation toolkit for codons in coding sequences.
tags: [degenotate, population-genomics, annotation, codon, selection]
author: oxo-call-community
source_url: "https://github.com/harvardinformatics/degenotate"
---

## Concepts

- **Tool Overview**: degenotate - Toolkit for annotating codon degeneracy in coding sequences for selection analyses.
- **Core Function**: Annotates codon positions by degeneracy level (0-fold, 2-fold, 4-fold) for population genetics analyses.
- **Input/Output**: Expects GFF annotation and FASTA sequences; outputs degeneracy annotations.
- **Installation**: `conda install -c bioconda degenotate`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly formatted GFF and matching FASTA files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `degenotate --gff annotation.gff --fasta genome.fa --output degen.tsv`
**Explanation:** Annotates codon degeneracy for all coding sequences.
