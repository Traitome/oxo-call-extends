---
name: clustalo
category: formatting
description: Fast and accurate multiple sequence alignment for DNA or proteins
tags: [clustalo, multiple-sequence-alignment, msa, protein, dna, phylogenetics]
author: oxo-call-community
source_url: "http://www.clustal.org/omega"
---

## Concepts

- **Tool Overview**: Clustal Omega is the latest version of the Clustal multiple sequence alignment program, offering improved accuracy and scalability for large datasets.
- **Core Function**: Aligns multiple DNA or protein sequences using HMM-based profile-profile alignment, suitable for thousands of sequences.
- **Input/Output**: Input: FASTA format sequences. Output: Aligned sequences in FASTA, CLUSTAL, PHYLIP, or other formats.
- **HMM Profiles**: Uses hidden Markov models for profile-profile alignment, improving accuracy for divergent sequences.
- **Scalability**: Can align tens of thousands of sequences, making it suitable for large-scale phylogenetic analyses.
- **Threading**: Supports multi-threading with `--threads` for faster alignment of large datasets.

## Pitfalls

- **Sequence Type**: Automatically detects DNA vs protein. Mixed types cause errors.
- **Large Datasets**: Very large alignments (>50,000 sequences) may require significant memory. Use `--maxiterate` to limit iterations.
- **Output Format**: Default is CLUSTAL format. Use `--outfmt` for other formats like FASTA or PHYLIP.
- **Guide Tree**: Generates guide tree internally. For custom trees, use `--guidetree-in`.
- **Iteration Count**: Default iterations work well for most cases. Increase `--maxiterate` for difficult alignments.

## Examples

### Basic protein alignment
**Args:** `-i sequences.fasta -o aligned.fasta --outfmt fasta`
**Explanation:** Aligns protein sequences and outputs in FASTA format for downstream analysis.

### Align DNA sequences
**Args:** `-i dna_sequences.fasta -o aligned.fasta --seqtype DNA --outfmt fasta`
**Explanation:** Explicitly specifies DNA sequence type and outputs FASTA format alignment.

### Align with multiple threads
**Args:** `-i sequences.fasta -o aligned.fasta --threads 8`
**Explanation:** Uses 8 threads for faster alignment of large sequence sets.

### Output in PHYLIP format
**Args:** `-i sequences.fasta -o aligned.phy --outfmt phy`
**Explanation:** Outputs alignment in PHYLIP format for use with phylogenetic software like RAxML or IQ-TREE.

### Generate guide tree
**Args:** `-i sequences.fasta -o aligned.fasta --guidetree-out tree.nwk`
**Explanation:** Saves the guide tree used for alignment in Newick format for inspection or reuse.

### Use custom guide tree
**Args:** `-i sequences.fasta -o aligned.fasta --guidetree-in tree.nwk`
**Explanation:** Uses a pre-computed guide tree instead of generating one, useful for consistent alignments.

### Align with more iterations
**Args:** `-i sequences.fasta -o aligned.fasta --maxiterate 5`
**Explanation:** Increases iteration count for potentially better alignment of difficult sequences.

### Dealign input sequences
**Args:** `-i aligned_input.fasta -o realigned.fasta --dealign`
**Explanation:** Removes existing alignment before realigning, useful when re-aligning previously aligned sequences.

### Force full alignment
**Args:** `-i sequences.fasta -o aligned.fasta --full`
**Explanation:** Forces full alignment even for very large datasets, bypassing fast approximate mode.

### Output statistics
**Args:** `-i sequences.fasta -o aligned.fasta --stats`
**Explanation:** Outputs alignment statistics including sequence lengths and gaps.
