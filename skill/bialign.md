---
name: bialign
category: alignment
description: Bialignment of RNAs and proteins
tags: [alignment, rna, protein, structural-alignment]
author: oxo-call-community
source_url: "https://github.com/s-will/BiAlign"
---

## Concepts
- **Tool Overview**: BiAlign is a tool for bialignment of RNA and protein sequences, performing simultaneous alignment along two dimensions (e.g., sequence and structure).
- **Bialignment**: Performs alignment considering two scoring dimensions simultaneously, which is useful for structural RNA alignment where both sequence and secondary structure matter.
- **Applications**: RNA structural alignment, protein structure comparison, and conserved RNA motif detection.
- **Algorithm**: Uses dynamic programming with combined scoring for sequence and structure features.

## Pitfalls
- **Computational Cost**: Bialignment is more computationally expensive than standard sequence alignment.
- **Structure Input**: For RNA alignment, secondary structure information or predictions may be required.
- **Parameter Tuning**: Scoring weights between sequence and structure dimensions need careful tuning.

## Examples
### Align two RNA sequences
**Args:** `bialign --seq1 rna1.fa --seq2 rna2.fa --out alignment.txt`
**Explanation:** Performs bialignment of two RNA sequences considering both sequence and structure.

### Align with structure input
**Args:** `bialign --seq1 rna1.fa --seq2 rna2.fa --struct1 rna1.stk --struct2 rna2.stk`
**Explanation:** Performs bialignment using provided secondary structure information.
