---
name: c4counter
category: annotation
description: Returns the number and types of human C4 regions in a FASTA file
tags: [c4counter, human, c4, annotation, hla]
author: oxo-call-community
source_url: "https://github.com/irunonayran/c4counter"
---

## Concepts

- **Tool Overview**: C4counter counts human C4 gene regions from FASTA files.
- **Core Function**: Identifies and counts C4 gene types (C4A, C4B) in assembled sequences.
- **Input**: Assembled genome or targeted C4 region FASTA.
- **Output**: Count and type of C4 genes detected.
- **Application**: HLA typing and immune gene analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda c4counter`

## Pitfalls

- **Human Specific**: Designed for human C4 gene analysis.
- **Assembly Quality**: Requires good quality assembly of C4 region.
- **Gene Complexity**: C4 region has complex structural variation.

## Examples

### Count C4 genes
**Args:** `c4counter -i c4_region.fa -o c4_counts.tsv`
**Explanation:** Counts C4A and C4B genes in the provided FASTA file.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
