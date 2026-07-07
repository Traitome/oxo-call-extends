---
name: fracsim
category: utility
description: A FracMinHash-based genome similarity estimator for bacteria.
tags: [fracsim, FracMinHash, genome similarity, bacteria]
author: oxo-call-community
source_url: "https://github.com/zhuyu534/FracSim"
---

## Concepts
- **FracMinHash**: Uses FracMinHash sketching for efficient similarity estimation.
- **Genome Comparison**: Compares bacterial genomes based on k-mer similarity.
- **Sketch-based**: Builds compact sketches of genomic sequences.
- **Scalable**: Efficiently handles large collections of genomes.
- **Phylogenetic Analysis**: Supports phylogenetic tree construction.

## Pitfalls
- **K-mer Selection**: K-mer size significantly affects results.
- **Genome Quality**: Requires complete or high-quality draft genomes.
- **Memory Usage**: Building sketches for many genomes requires memory.
- **Sketch Size**: Small sketch sizes may reduce accuracy.
- **Taxonomic Bias**: May have bias towards certain bacterial groups.

## Examples
### Compute pairwise similarity
**Args:** `fracsim compare genome1.fasta genome2.fasta -o similarity.txt`
**Explanation:** Computes similarity between two bacterial genomes.

### Build sketch
**Args:** `fracsim sketch genome.fasta -o genome.sketch`
**Explanation:** Creates a FracMinHash sketch of the genome.

### Compare multiple genomes
**Args:** `fracsim compare --list genomes.txt -o matrix.txt`
**Explanation:** Computes similarity matrix for multiple genomes.

### Build phylogenetic tree
**Args:** `fracsim tree --list genomes.txt -o tree.nwk`
**Explanation:** Constructs phylogenetic tree based on similarity.

### Adjust k-mer size
**Args:** `fracsim sketch -k 31 genome.fasta -o genome.sketch`
**Explanation:** Creates sketch using k-mer size 31.