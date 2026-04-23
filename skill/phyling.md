---
name: phyling
category: population-genomics
description: A phylogenetic inference tool based on protein-coding genomic sequences
tags: [phyling, population-genomics]
author: oxo-call-community
source_url: "https://github.com/stajichlab/Phyling"
---

## Concepts
- **Tool Overview**: Phyling is a fast, scalable, and user-friendly tool supporting phylogenomic reconstruction of species phylogenies directly from protein-encoded genomic data. It identifies orthologous genes by searching a sample's protein sequences against a Hidden Markov Models marker set, containing single-copy orthologs, retrieved from the BUSCO database. In the final step, users can choose between consensus and concatenation strategies to construct the species tree from the aligned orthologs.
- **Core Function**: A phylogenetic inference tool based on protein-coding genomic sequences
- **Input/Output**: FASTA/BAM/SAM/GFF/GTF
- **Installation**: `conda install -c bioconda phyling`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
