---
name: ucsc-farc
category: utility
description: UCSC faRc - Tool for reverse complementing FASTA sequences.
tags: [ucsc-farc, ucsc, fasta, sequence-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faRc - A tool for reverse complementing FASTA sequences.
- **Core Function**: Produces reverse complement of sequences.
- **Input**: FASTA file.
- **Output**: Reverse complemented FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence analysis, strand conversion, primer design.

## Pitfalls

- **Ambiguity Codes**: May not handle all ambiguity codes correctly.
- **Memory**: May require significant memory for large sequences.

## Examples

### Reverse complement
**Args:** `faRc input.fa > rc.fa`
**Explanation:** Reverse complement sequences.

### From stdin
**Args:** `cat input.fa | faRc > rc.fa`
**Explanation:** Reverse complement from piped input.
