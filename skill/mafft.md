---
name: mafft
category: alignment
description: Multiple alignment program for amino acid or nucleotide sequences based on fast Fourier transform
tags: [mafft, alignment, multiple-sequence-alignment, FFT]
author: oxo-call-community
source_url: "http://mafft.cbrc.jp/alignment/software/"
---

## Concepts

- **Tool Overview**: mafft v7.525 - A powerful multiple sequence alignment program for amino acid or nucleotide sequences using fast Fourier transform (FFT) for efficient sequence comparison.
- **Core Function**: Performs accurate multiple sequence alignments using various strategies optimized for speed and accuracy.
- **Input/Output**: Input: FASTA format sequence files; Output: Aligned sequences in FASTA, Clustal, or other formats.
- **Installation**: `conda install -c bioconda mafft`
- **Alignment Strategies**: Supports multiple strategies including FFT-NS-1, FFT-NS-2, L-INS-i, E-INS-i, G-INS-i, and more.
- **FFT-based Alignment**: Uses fast Fourier transform to efficiently calculate sequence similarities.

## Pitfalls

- **Memory Usage**: Large alignments may require significant memory resources.
- **Time Complexity**: Progressive alignment strategies can be slow for very large datasets.
- **Parameter Selection**: Choosing the wrong alignment strategy can affect accuracy.
- **Sequence Length**: Extreme differences in sequence lengths can affect alignment quality.
- **Ambiguous Characters**: Mixed sequence types (nucleotide/amino acid) cause errors.
- **Output Format**: Incorrect format specification may produce unusable output.

## Examples

### Automatic alignment strategy
**Args:** `mafft --auto input.fasta > aligned.fasta`
**Explanation:** Automatically selects the best alignment strategy based on data size.

### L-INS-i for accurate alignment
**Args:** `mafft --localpair --maxiterate 1000 input.fasta > aligned.fasta`
**Explanation:** Uses local pairwise alignment with 1000 iterations for high accuracy.

### E-INS-i for sequences with conserved domains
**Args:** `mafft --ep 0 --genafpair --maxiterate 1000 input.fasta > aligned.fasta`
**Explanation:** For sequences with conserved domains and variable regions.

### Output in Clustal format
**Args:** `mafft --auto --clustalout input.fasta > aligned.clustal`
**Explanation:** Outputs alignment in Clustal format.

### With gap opening penalty
**Args:** `mafft --auto --op 10 --ep 0.1 input.fasta > aligned.fasta`
**Explanation:** Sets gap opening penalty to 10 and gap extension penalty to 0.1.

### Large dataset mode
**Args:** `mafft --parttree input.fasta > aligned.fasta`
**Explanation:** Uses parttree algorithm for faster alignment of large datasets.