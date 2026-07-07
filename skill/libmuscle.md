---
name: libmuscle
category: alignment
description: libMuscle - MUSCLE sequence alignment library
tags: [libmuscle, alignment, sequence-alignment, MUSCLE, bioinformatics]
author: oxo-call-community
source_url: "http://darlinglab.org/mauve"
---

## Concepts

- **Sequence Alignment**: Multiple sequence alignment algorithms
- **MUSCLE Algorithm**: Implementation of MUSCLE alignment algorithm
- **Profile Alignment**: Profile-profile alignment support
- **Phylogenetic Trees**: Guide tree construction
- **Iterative Refinement**: Iterative alignment refinement
- **High Performance**: Optimized for speed and accuracy

## Pitfalls

- **Memory Usage**: Memory-intensive for large alignments
- **Computational Time**: May be slow for very large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Format Compatibility**: Specific input format required
- **Version Compatibility**: API may change between versions
- **Thread Safety**: Not thread-safe by default

## Examples

### Align sequences
**Args:** `muscle align -i sequences.fasta -o aligned.fasta`
**Explanation:** Performs multiple sequence alignment.

### Profile alignment
**Args:** `muscle profile -i1 profile1.txt -i2 profile2.txt -o combined.txt`
**Explanation:** Aligns two profiles.

### Build guide tree
**Args:** `muscle tree -i sequences.fasta -o tree.nwk`
**Explanation:** Constructs guide tree.

### Refine alignment
**Args:** `muscle refine -i aligned.fasta -o refined.fasta`
**Explanation:** Refines existing alignment.

### Fast mode
**Args:** `muscle align -i sequences.fasta -o aligned.fasta -fast`
**Explanation:** Uses fast alignment mode.

### Statistics
**Args:** `muscle stats -i aligned.fasta`
**Explanation:** Shows alignment statistics.