---
name: ucsc-fasize
category: utility
description: UCSC faSize - Tool for calculating FASTA sequence sizes.
tags: [ucsc-fasize, ucsc, fasta, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faSize - A tool for calculating sizes of FASTA sequences.
- **Core Function**: Reports total bases and sequence lengths.
- **Input**: FASTA file.
- **Output**: Size statistics.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence statistics, genome analysis, quality control.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **Ambiguity Codes**: May not count ambiguous bases correctly.

## Examples

### Calculate sizes
**Args:** `faSize genome.fa > sizes.txt`
**Explanation:** Calculate sequence sizes.

### With detailed output
**Args:** `faSize -detailed genome.fa > sizes.txt`
**Explanation:** Detailed size information.
