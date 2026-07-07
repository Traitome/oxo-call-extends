---
name: translatorx
category: analysis
description: TranslatorX - Tool for aligning protein-coding DNA sequences.
tags: [translatorx, sequence-alignment, codon-alignment, phylogenetics, dna]
author: oxo-call-community
source_url: "https://github.com/enyojs/translatorx"
---

## Concepts

- **Tool Overview**: TranslatorX - A tool for aligning protein-coding DNA sequences by translating to proteins first.
- **Core Function**: Aligns DNA sequences by translating to amino acids, aligning proteins, and back-translating.
- **Input**: DNA sequences (FASTA), genetic code table.
- **Output**: Aligned DNA sequences, protein alignments, codon-based alignment.
- **Installation**: `pip install translatorx`
- **Use Case**: Phylogenetic analysis, sequence comparison, molecular evolution.

## Pitfalls

- **Frame Shifts**: Requires correct reading frame for accurate alignment.
- **Ambiguity Codes**: May have issues with ambiguous nucleotide codes.

## Examples

### Align coding sequences
**Args:** `translatorx -i dna.fasta -o aligned.fasta`
**Explanation:** Align protein-coding DNA sequences.

### With custom genetic code
**Args:** `translatorx -i sequences.fasta -g 11 -o codon_aligned.fasta`
**Explanation:** Align sequences using specific genetic code.
