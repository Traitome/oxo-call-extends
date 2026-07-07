---
name: ucsc-getrna
category: utility
description: UCSC getRna - Tool for extracting RNA sequences.
tags: [ucsc-getrna, ucsc, rna-seq, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC getRna - A tool for extracting RNA sequences from gene predictions.
- **Core Function**: Extracts spliced RNA sequences from genome.
- **Input**: Gene prediction file, genome FASTA.
- **Output**: RNA sequences.
- **Installation**: Part of UCSC utilities
- **Use Case**: RNA analysis, transcriptomics, gene expression.

## Pitfalls

- **FASTA Requirement**: Requires genome FASTA file.
- **Memory**: May require significant memory for large genomes.

## Examples

### Extract RNA sequences
**Args:** `getRna genes.txt genome.fa > rna.fa`
**Explanation:** Extract RNA sequences from gene predictions.

### With options
**Args:** `getRna -cdsOnly genes.txt genome.fa > cds.fa`
**Explanation:** Extract only CDS regions.
