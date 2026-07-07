---
name: ucsc-fanoise
category: utility
description: UCSC faNoise - Tool for adding noise to FASTA sequences.
tags: [ucsc-fanoise, ucsc, fasta, sequence-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faNoise - A tool for adding random noise to FASTA sequences.
- **Core Function**: Introduces random mutations into sequences.
- **Input**: FASTA file.
- **Output**: Noisy FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Simulation, testing, error analysis.

## Pitfalls

- **Mutation Rate**: Requires appropriate mutation rate setting.
- **Determinism**: May not produce reproducible results without seed.

## Examples

### Add noise
**Args:** `faNoise -rate=0.01 input.fa > noisy.fa`
**Explanation:** Add 1% random mutations.

### With seed
**Args:** `faNoise -rate=0.01 -seed=123 input.fa > noisy.fa`
**Explanation:** Add noise with fixed seed.
