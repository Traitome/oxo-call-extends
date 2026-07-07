---
name: ucsc-oligomatch
category: utility
description: UCSC oligoMatch - Tool for finding oligonucleotide matches.
tags: [ucsc-oligomatch, ucsc, oligonucleotide, matching, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC oligoMatch - A tool for finding oligonucleotide matches.
- **Core Function**: Finds matches of oligonucleotides in sequences.
- **Input**: Oligo file, sequence file.
- **Output**: Match locations.
- **Installation**: Part of UCSC utilities
- **Use Case**: Primer design, sequence analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **Format Requirements**: Requires proper input format.

## Examples

### Find oligonucleotide matches
**Args:** `oligoMatch oligos.txt genome.fa > matches.txt`
**Explanation:** Find oligo matches in genome.

### With options
**Args:** `oligoMatch -minScore=10 oligos.txt genome.fa > matches.txt`
**Explanation:** Minimum match score.
