---
name: dashing2
category: utility
description: Dashing2 - fast toolkit for k-mer and minimizer encoding, sketching, and comparison
tags: [dashing2, utility, k-mer, sketching, sequence-comparison]
author: oxo-call-community
source_url: "https://github.com/dnbaker/dashing2/blob/v2.1.20/README.md"
---

## Concepts

- **Tool Overview**: dashing2 (v2.1.20+) is a fast toolkit for k-mer and minimizer encoding, sketching, comparison, and indexing.
- **Core Function**: Computes sequence similarity using k-mer sketches and minimizer-based approaches.
- **Input/Output**: Input: FASTA sequences. Output: Distance matrices, sketches, indexes.
- **Algorithm**: Uses minimizer sampling and locality-sensitive hashing for fast comparison.
- **Key Features**: Fast sequence comparison, sketch-based indexing, supports large datasets.
- **Installation**: `conda install -c bioconda dashing2`

## Pitfalls

- **k-mer Selection**: k-mer size affects sensitivity and speed.
- **Sketch Size**: Larger sketches improve accuracy but increase memory usage.
- **Memory Constraints**: Very large datasets may require careful memory management.
- **Sequence Composition**: Results may vary with different sequence compositions.
- **Comparison Metrics**: Different metrics have different computational requirements.

## Examples

### Compute sequence similarity
**Args:** `dashing2 sketch -i genome.fasta -o genome.sketch`
**Explanation:** Create minimizer sketch from genome sequence.

### Compare sequences
**Args:** `dashing2 compare -i genome1.sketch genome2.sketch -o distance.txt`
**Explanation:** Compute distance between two sequence sketches.

### Build index
**Args:** `dashing2 index -i genomes/ -o index/ --kmer-size 21`
**Explanation:** Build k-mer index from multiple genomes with k=21.
