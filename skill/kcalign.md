---
name: kcalign
category: alignment
description: Kalgin-based codon-aware aligner for multiple sequences.
tags: [kcalign, alignment, codon-aware, MSA, protein]
author: oxo-call-community
source_url: "https://github.com/davebx/kc-align/blob/master/README.md"
---

## Concepts

- **Tool Overview**: kcalign (v1.0.2) - Codon-aware multiple sequence aligner based on Kalgin.
- **Codon Awareness**: Takes codon structure into account during alignment.
- **Protein-Coding Focus**: Optimized for protein-coding sequences.
- **Frame Preservation**: Maintains reading frame during alignment.
- **Multiple Sequences**: Handles multiple sequences simultaneously.
- **Gap Handling**: Intelligent gap placement preserving codon structure.

## Pitfalls

- **Input Requirements**: Requires coding sequences as input.
- **Frame Shifts**: Frame shifts in input can cause issues.
- **Sequence Length**: Variable sequence lengths may affect alignment.
- **Memory Usage**: Large datasets require memory.
- **Time Complexity**: Complex alignments can be slow.
- **Format Compatibility**: Limited input format support.

## Examples

### Align coding sequences
**Args:** `kcalign -i sequences.fasta -o aligned.fasta`
**Explanation:** Aligns codon sequences preserving reading frame.

### Output in Clustal format
**Args:** `kcalign -i sequences.fasta -o aligned.clustal -f clustal`
**Explanation:** Outputs alignment in Clustal format.

### Force reading frame
**Args:** `kcalign -i sequences.fasta -o aligned.fasta -f 1`
**Explanation:** Forces alignment in reading frame 1.

### Verbose mode
**Args:** `kcalign -i sequences.fasta -o aligned.fasta -v`
**Explanation:** Shows verbose output during alignment.

### Gap penalty adjustment
**Args:** `kcalign -i sequences.fasta -o aligned.fasta -g 10`
**Explanation:** Sets gap penalty to 10.

### Quality filtering
**Args:** `kcalign -i sequences.fasta -o aligned.fasta -q 20`
**Explanation:** Filters low-quality sequences.