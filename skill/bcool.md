---
name: bcool
category: utility
description: BCOOL - Read corrector for NGS sequencing data using de Bruijn graph alignment
tags: [error-correction, read-correction, de-bruijn-graph, ngs]
author: oxo-call-community
source_url: "https://github.com/Malfoy/BCOOL"
---

## Concepts

- **Tool Overview**: BCOOL corrects sequencing errors in NGS reads by aligning them to a de Bruijn graph.

- **Graph-Based**: Uses de Bruijn graph alignment for error correction, leveraging k-mer information.

- **Error Correction**: Corrects substitution errors, improving read quality for downstream analysis.

- **Assembly Improvement**: Corrected reads improve assembly quality and contiguity.

## Pitfalls

- **K-mer Size**: K-mer size affects correction sensitivity. Adjust for data characteristics.

- **Coverage**: Low coverage regions may have reduced correction effectiveness.

- **Memory Usage**: De Bruijn graph construction requires substantial memory for large datasets.

## Examples

### Basic read correction
**Args:** `bcool -in reads.fasta -kmer-size 31 -out corrected.fasta`
**Explanation:** Corrects errors in reads using de Bruijn graph with k=31.

### Specify abundance threshold
**Args:** `bcool -in reads.fasta -kmer-size 31 -abundance 2 -out corrected.fasta`
**Explanation:** Uses minimum abundance threshold to filter errors.
