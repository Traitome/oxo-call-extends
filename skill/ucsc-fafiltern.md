---
name: ucsc-fafiltern
category: utility
description: UCSC faFilterN - Tool for filtering Ns in FASTA sequences.
tags: [ucsc-fafiltern, ucsc, fasta, sequence-filtering, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faFilterN - A tool for filtering sequences by N content.
- **Core Function**: Removes sequences with high N content.
- **Input**: FASTA file.
- **Output**: Filtered FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence filtering, quality control, genome assembly.

## Pitfalls

- **Threshold Setting**: Requires appropriate N content threshold.
- **Memory**: May require significant memory for large sequences.

## Examples

### Filter by N content
**Args:** `faFilterN -maxN=0.05 input.fa > filtered.fa`
**Explanation:** Remove sequences with >5% N content.

### With options
**Args:** `faFilterN -maxN=0.1 -minSize=1000 input.fa > filtered.fa`
**Explanation:** Filter by N content and size.
