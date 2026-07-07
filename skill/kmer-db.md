---
name: kmer-db
category: utility
description: A fast and memory-efficient tool for estimating evolutionary distances
tags: [kmer-db, utility, evolutionary-distance, phylogeny, k-mer]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/kmer-db"
---

## Concepts

- **Evolutionary Distance Estimation**: Estimates genetic distances between sequences
- **K-mer Based**: Uses k-mer frequencies for rapid distance calculation
- **Memory Efficiency**: Optimized for large-scale comparative genomics
- **Phylogenetic Analysis**: Supports phylogenetic tree construction
- **Batch Comparison**: Compares multiple genomes efficiently
- **Reference-free**: Works without requiring sequence alignment

## Pitfalls

- **K-mer Selection**: K-mer size affects distance estimation accuracy
- **Genome Similarity**: Similar genomes may have inflated distance estimates
- **Horizontal Transfer**: Gene transfer events affect distance calculations
- **Database Size**: Large numbers of genomes increase computation time
- **Memory Requirements**: Very large datasets require significant memory
- **Interpretation**: Distance metrics require careful biological interpretation

## Examples

### Build k-mer database
**Args:** `kmer-db build -i genomes/ -o database.kmcdb`
**Explanation:** Builds a k-mer database from genome sequences.

### Estimate pairwise distances
**Args:** `kmer-db distance -d database.kmcdb -o distances.tsv`
**Explanation:** Estimates evolutionary distances between all genome pairs.

### Compare specific genomes
**Args:** `kmer-db compare -d database.kmcdb -g genome1.fna -g genome2.fna`
**Explanation:** Compares two specific genomes.

### Build phylogenetic tree
**Args:** `kmer-db tree -d database.kmcdb -o tree.nwk`
**Explanation:** Constructs a neighbor-joining phylogenetic tree.

### Filter by k-mer frequency
**Args:** `kmer-db distance -d database.kmcdb -o distances.tsv --min-freq 3`
**Explanation:** Only uses k-mers with frequency >= 3.

### Export distance matrix
**Args:** `kmer-db export -d database.kmcdb -o matrix.tsv`
**Explanation:** Exports distance matrix for external analysis tools.