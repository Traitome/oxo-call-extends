---
name: translatory
category: utility
description: Translatory - Tool for translating nucleic acid sequences.
tags: [translatory, translation, dna-to-protein, bioinformatics, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/compbio/translatory"
---

## Concepts

- **Tool Overview**: Translatory - A tool for translating DNA/RNA sequences to protein sequences.
- **Core Function**: Translates nucleic acid sequences to amino acid sequences using standard or custom genetic codes.
- **Input**: Nucleic acid sequences (FASTA), optional genetic code specification.
- **Output**: Protein sequences (FASTA), translation frames, ORFs.
- **Installation**: `pip install translatory` or `conda install -c bioconda translatory`
- **Use Case**: Sequence analysis, gene prediction, proteomics.

## Pitfalls

- **Frame Selection**: Requires correct reading frame for meaningful translation.
- **Stop Codons**: May encounter premature stop codons.

## Examples

### Translate DNA
**Args:** `translatory -i dna.fasta -o protein.fasta`
**Explanation:** Translate DNA sequences to protein sequences.

### All frames
**Args:** `translatory -i sequence.fasta --all-frames -o translations/`
**Explanation:** Translate all six reading frames.
