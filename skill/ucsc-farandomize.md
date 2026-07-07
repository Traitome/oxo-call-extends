---
name: ucsc-farandomize
category: utility
description: UCSC faRandomize - Tool for randomizing FASTA sequences.
tags: [ucsc-farandomize, ucsc, fasta, sequence-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faRandomize - A tool for randomizing FASTA sequences.
- **Core Function**: Shuffles nucleotides while maintaining composition.
- **Input**: FASTA file.
- **Output**: Randomized FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Negative control, sequence shuffling, simulation.

## Pitfalls

- **Seed Setting**: May not produce reproducible results without seed.
- **Composition**: Maintains original nucleotide composition.

## Examples

### Randomize sequence
**Args:** `faRandomize input.fa > randomized.fa`
**Explanation:** Shuffle sequence nucleotides.

### With seed
**Args:** `faRandomize -seed=456 input.fa > randomized.fa`
**Explanation:** Randomize with fixed seed.
