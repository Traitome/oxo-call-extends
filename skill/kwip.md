---
name: kwip
category: population-genomics
description: De novo alignment-free genetic dissimilarity measure using k-mer weighted inner products
tags: [kwip, population-genomics, k-mer, genetic-dissimilarity, alignment-free]
author: oxo-call-community
source_url: "https://github.com/kdmurray91/kWIP"
---

## Concepts

- **K-mer Weights**: Uses weighted k-mer counts for analysis
- **Alignment-free**: No sequence alignment required
- **Genetic Dissimilarity**: Measures genetic dissimilarity between samples
- **De novo Analysis**: Works without reference genome
- **Population Genomics**: Designed for population-level analysis
- **Fast Computation**: Efficient k-mer based computation

## Pitfalls

- **K-mer Size**: K-mer size affects dissimilarity estimates
- **Hash Independence**: Different hash functions give different results
- **Sample Depth**: Coverage differences affect k-mer counts
- **Genome Size**: Large genomes need more k-mers
- **Memory Usage**: Large populations require significant memory
- **Normalization**: Proper normalization is critical

## Examples

### Compute distance matrix
**Args:** `kwip -k hash1.kwip -k hash2.kwip -o dist_matrix.txt`
**Explanation:** Computes weighted inner product distance.

### Create hash files
**Args:** `kwip hash -i sample1.fastq -o sample1.kwip`
**Explanation:** Creates k-mer hash for a sample.

### Batch distance computation
**Args:** `kwip dist -k samples.txt -o distance_matrix.tsv`
**Explanation:** Computes distances for multiple samples.

### Specify k-mer size
**Args:** `kwip hash -i sample.fastq -k 21 -o sample.kwip`
**Explanation:** Uses k-mer size of 21 for hashing.

### Export tree
**Args:** `kwip tree -i distance_matrix.tsv -o phylogeny.nwk`
**Explanation:** Generates neighbor-joining tree.

### Filter k-mers
**Args:** `kwip hash -i sample.fastq --min-count 5 -o filtered.kwip`
**Explanation:** Only includes k-mers with count >= 5.