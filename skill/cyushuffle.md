---
name: cyushuffle
category: utility
description: Cython wrapper over uShuffle - shuffling biological sequences while preserving k-let counts
tags: [cyushuffle, utility, sequence-analysis, shuffling, k-mer]
author: oxo-call-community
source_url: "https://cs.usu.edu/people/MinghuiJiang/ushuffle/"
---

## Concepts

- **Tool Overview**: cyushuffle (v1.1.2+) is a Cython wrapper over uShuffle for shuffling biological sequences while preserving k-mer counts.
- **Core Function**: Generates random permutations of sequences while maintaining the frequency of k-mers.
- **Input/Output**: Input: FASTA/FASTQ sequences. Output: Shuffled sequences with preserved k-mer composition.
- **Algorithm**: Uses a Markov chain approach to shuffle sequences while preserving k-let counts.
- **Key Features**: Fast shuffling, preserves sequence composition, supports custom k-mer sizes.
- **Installation**: `conda install -c bioconda cyushuffle`

## Pitfalls

- **k-mer Selection**: k-mer size affects shuffling quality and computational time.
- **Sequence Length**: Very short sequences may not produce meaningful shuffles.
- **Memory Usage**: Large datasets may require significant memory.
- **Random Seed**: Results are deterministic with fixed seed; use different seeds for multiple shuffles.
- **Biological Context**: Shuffled sequences lose biological meaning; use carefully in statistical tests.

## Examples

### Shuffle FASTA sequences
**Args:** `cyushuffle -i input.fasta -o shuffled.fasta -k 2`
**Explanation:** Shuffle sequences while preserving di-nucleotide frequencies.

### Shuffle with custom k-mer size
**Args:** `cyushuffle -i input.fasta -o shuffled.fasta -k 3`
**Explanation:** Shuffle sequences preserving tri-nucleotide composition.

### Generate multiple shuffled sequences
**Args:** `cyushuffle -i input.fasta -o shuffled_ -k 2 -n 5`
**Explanation:** Generate 5 independent shuffled versions of input sequences.
