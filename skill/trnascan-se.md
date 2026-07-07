---
name: trnascan-se
category: analysis
description: tRNAscan-SE - Tool for detecting tRNA genes in genomic sequences.
tags: [trnascan-se, trna, gene-finding, genomics, bioinformatics]
author: oxo-call-community
source_url: "http://lowelab.ucsc.edu/tRNAscan-SE/"
---

## Concepts

- **Tool Overview**: tRNAscan-SE - A tool for detecting tRNA genes in genomic sequences.
- **Core Function**: Identifies tRNA genes using covariance models and sequence analysis.
- **Input**: Genome sequences (FASTA).
- **Output**: tRNA gene predictions with coordinates, anticodons, and scores.
- **Installation**: `conda install -c bioconda trnascan-se`
- **Use Case**: Genome annotation, tRNA gene identification, comparative genomics.

## Pitfalls

- **Pseudogenes**: May include pseudogenes in predictions.
- **Non-standard tRNAs**: May miss atypical tRNA genes.

## Examples

### Scan genome
**Args:** `tRNAscan-SE genome.fasta -o trnas.txt`
**Explanation:** Scan genome for tRNA genes.

### With GFF output
**Args:** `tRNAscan-SE -G genome.fasta -o trnas.gff`
**Explanation:** Output results in GFF format.
