---
name: treesapp
category: analysis
description: TreeSAPP - Tool for taxonomic classification of metagenomic sequences.
tags: [treesapp, metagenomics, taxonomic-classification, phylogenetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hallamlab/treesapp"
---

## Concepts

- **Tool Overview**: TreeSAPP - A tool for taxonomic classification of metagenomic sequences using phylogenetic placement.
- **Core Function**: Classifies sequences by placing them into reference phylogenetic trees.
- **Input**: Metagenomic reads (FASTQ), reference databases.
- **Output**: Taxonomic classifications, phylogenetic placements, abundance estimates.
- **Installation**: `pip install treesapp`
- **Use Case**: Metagenomics, microbial community analysis, environmental sequencing.

## Pitfalls

- **Database Size**: Requires large reference databases.
- **Computation Time**: May be slow for large datasets.

## Examples

### Classify sequences
**Args:** `treesapp assign -i reads.fastq -o classifications/`
**Explanation:** Classify metagenomic sequences using phylogenetic placement.

### Build database
**Args:** `treesapp build -i reference.fasta -o database/`
**Explanation:** Build custom reference database.
