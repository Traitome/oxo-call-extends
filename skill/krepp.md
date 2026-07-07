---
name: krepp
category: phylogenetics
description: K-mer-based maximum pseudo-likelihood method for estimating read distances and phylogenetic placement
tags: [krepp, phylogenetics, k-mer, phylogenetic-placement, distance-estimation]
author: oxo-call-community
source_url: "https://github.com/bo1929/krepp"
---

## Concepts

- **K-mer Based**: Uses k-mer frequencies for analysis
- **Maximum Pseudo-likelihood**: Estimates evolutionary distances
- **Phylogenetic Placement**: Places reads in reference phylogeny
- **Read Distance Estimation**: Estimates distances between reads
- **Whole Genome Analysis**: Handles genome-wide phylogenetic analysis
- **Efficient Computation**: Fast k-mer based computations

## Pitfalls

- **K-mer Size**: K-mer size affects distance estimation
- **Reference Quality**: Results depend on reference tree quality
- **Computational Resources**: Large datasets need significant memory
- **Novel Taxa**: Novel organisms may have poor placement
- **Model Assumptions**: Pseudo-likelihood has specific assumptions
- **Sequence Evolution**: Rate heterogeneity affects estimates

## Examples

### Estimate read distances
**Args:** `krepp distance -i reads.fastq -o distances.tsv`
**Explanation:** Estimates distances between reads using k-mers.

### Phylogenetic placement
**Args:** `krepp place -i reads.fastq -r reference_tree.nwk -o placement.txt`
**Explanation:** Places reads into reference phylogenetic tree.

### Specify k-mer size
**Args:** `krepp distance -i reads.fastq -k 31 -o distances.tsv`
**Explanation:** Uses k-mer size of 31 for analysis.

### Batch processing
**Args:** `krepp batch -d samples/ -o results/`
**Explanation:** Processes multiple read files in batch.

### Generate reference tree
**Args:** `krepp tree -i genomes/ -o reference_tree.nwk`
**Explanation:** Generates reference tree from genome sequences.

### Distance matrix
**Args:** `krepp matrix -i reads_dir/ -o distance_matrix.tsv`
**Explanation:** Creates pairwise distance matrix for samples.