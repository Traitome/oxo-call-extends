---
name: ucsc-facount
category: utility
description: UCSC faCount - Tool for counting bases in FASTA sequences.
tags: [ucsc-facount, ucsc, fasta, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faCount - A tool for counting nucleotide bases in FASTA sequences.
- **Core Function**: Counts A, C, G, T, N, and other bases in sequences.
- **Input**: FASTA file.
- **Output**: Base count statistics.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence analysis, quality control, genome statistics.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **Ambiguity Codes**: May not handle all ambiguity codes.

## Examples

### Count bases
**Args:** `faCount genome.fa > counts.txt`
**Explanation:** Count bases in FASTA file.

### With options
**Args:** `faCount -verbose genome.fa > counts.txt`
**Explanation:** Count with detailed output.
