---
name: ucsc-fafrag
category: utility
description: UCSC faFrag - Tool for extracting fragments from FASTA.
tags: [ucsc-fafrag, ucsc, fasta, sequence-extraction, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faFrag - A tool for extracting sequence fragments from FASTA.
- **Core Function**: Extracts specific regions from sequences.
- **Input**: FASTA file, BED file with regions.
- **Output**: Extracted fragments.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence extraction, region analysis, primer design.

## Pitfalls

- **Coordinate Format**: Requires proper coordinate specification.
- **Memory**: May require significant memory for large sequences.

## Examples

### Extract fragments
**Args:** `faFrag genome.fa regions.bed > fragments.fa`
**Explanation:** Extract regions from genome.

### With options
**Args:** `faFrag -mask genome.fa regions.bed > fragments.fa`
**Explanation:** Extract with soft masking.
