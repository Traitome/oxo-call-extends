---
name: dashing
category: assembly
description: Fast and accurate genomic distances using HyperLogLog
tags: [dashing, assembly, k-mer, distance-calculation, HyperLogLog]
author: oxo-call-community
source_url: "https://github.com/dnbaker/dashing"
---

## Concepts

- **Tool Overview**: dashing (v1.0+) is a tool for fast and accurate genomic distance calculation using HyperLogLog sketches.
- **Core Function**: Computes sequence similarity and distance metrics between genomic sequences efficiently.
- **Input/Output**: Input: FASTA sequences. Output: Distance matrices, similarity scores.
- **Algorithm**: Uses HyperLogLog sketching and k-mer counting for efficient distance estimation.
- **Key Features**: Fast computation, memory-efficient, handles large genomes.
- **Installation**: `conda install -c bioconda dashing`

## Pitfalls

- **k-mer Selection**: k-mer size affects distance estimation accuracy.
- **Sketch Size**: Larger sketches improve accuracy but increase memory usage.
- **Genome Size**: Performance may vary with very large genomes.
- **Memory Constraints**: May require careful memory management for large datasets.
- **Normalization**: Results require proper normalization for comparison.

## Examples

### Compute genomic distance
**Args:** `dashing dist -i genome1.fasta genome2.fasta -o distance.txt`
**Explanation:** Compute distance between two genomes using HyperLogLog.

### Compare multiple genomes
**Args:** `dashing dist -i genomes/*.fasta -o distance_matrix.txt`
**Explanation:** Compute pairwise distances between multiple genomes.

### Use specific k-mer size
**Args:** `dashing dist -i genome1.fasta genome2.fasta -k 21 -o distance.txt`
**Explanation:** Compute distance using k-mer size of 21.
