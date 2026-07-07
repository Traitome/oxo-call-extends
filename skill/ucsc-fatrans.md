---
name: ucsc-fatrans
category: utility
description: UCSC faTrans - Tool for translating FASTA sequences.
tags: [ucsc-fatrans, ucsc, fasta, translation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faTrans - A tool for translating nucleotide sequences.
- **Core Function**: Translates DNA sequences to protein sequences.
- **Input**: Nucleotide FASTA file.
- **Output**: Protein FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence translation, protein analysis, gene prediction.

## Pitfalls

- **Frame Selection**: Requires correct reading frame.
- **Stop Codons**: May produce truncated proteins.

## Examples

### Translate sequences
**Args:** `faTrans input.fa > output.pep`
**Explanation:** Translate DNA to protein.

### With frame
**Args:** `faTrans -frame=2 input.fa > output.pep`
**Explanation:** Translate with specific reading frame.
