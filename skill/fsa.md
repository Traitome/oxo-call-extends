---
name: fsa
category: alignment
description: FSA is a probabilistic multiple sequence alignment algorithm which uses a "distance-based" approach to aligning homologous protein, RNA or DNA sequences.
tags: [fsa, multiple sequence alignment, probabilistic, distance-based]
author: oxo-call-community
source_url: "http://fsa.sourceforge.net/"
---

## Concepts
- **Probabilistic Alignment**: Uses probabilistic models for sequence alignment.
- **Distance-based Approach**: Computes alignments based on sequence distances.
- **Homology Detection**: Identifies homologous regions across sequences.
- **Gap Handling**: Sophisticated gap insertion and extension scoring.
- **Profile Alignment**: Supports profile-based multiple sequence alignment.

## Pitfalls
- **Computational Complexity**: Slow for large sequence sets.
- **Memory Requirements**: High memory usage for large alignments.
- **Parameter Sensitivity**: Results depend on parameter settings.
- **Sequence Length**: May struggle with very long sequences.
- **Output Format**: Limited output format options.

## Examples
### Basic multiple alignment
**Args:** `fsa sequences.fasta -o alignment.fasta`
**Explanation:** Aligns sequences using default parameters.

### RNA alignment
**Args:** `fsa -r rna_sequences.fasta -o rna_alignment.fasta`
**Explanation:** Aligns RNA sequences with RNA-specific scoring.

### Protein alignment
**Args:** `fsa -p proteins.fasta -o protein_alignment.fasta`
**Explanation:** Aligns protein sequences using BLOSUM matrix.

### Output in Clustal format
**Args:** `fsa sequences.fasta -f clustal -o alignment.clustal`
**Explanation:** Outputs alignment in Clustal format.

### With custom gap penalties
**Args:** `fsa -g -10 -e -2 sequences.fasta -o alignment.fasta`
**Explanation:** Sets custom gap opening (-10) and extension (-2) penalties.