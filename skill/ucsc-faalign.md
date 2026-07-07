---
name: ucsc-faalign
category: utility
description: UCSC faAlign - Tool for aligning FASTA sequences.
tags: [ucsc-faalign, ucsc, sequence-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faAlign - A tool for pairwise alignment of FASTA sequences.
- **Core Function**: Aligns two sequences using dynamic programming.
- **Input**: Two FASTA sequences.
- **Output**: Alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence alignment, comparative genomics, sequence analysis.

## Pitfalls

- **Memory**: May require significant memory for long sequences.
- **Computation Time**: May be slow for large sequences.

## Examples

### Align sequences
**Args:** `faAlign target.fa query.fa > alignment.psl`
**Explanation:** Align two sequences.

### With parameters
**Args:** `faAlign -minScore=1000 target.fa query.fa > alignment.psl`
**Explanation:** Align with minimum score threshold.
