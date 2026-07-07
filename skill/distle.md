---
name: distle
category: population-genomics
description: distle - Fast distance matrix calculations on FASTA and cgMLST files.
tags: [distle, population-genomics, distance-matrix, cgmlst, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/KHajji/distle"
---

## Concepts

- **Tool Overview**: distle (v0.3.0+) is a fast distance matrix calculation tool for FASTA and cgMLST files.
- **Core Function**: Computes pairwise distances between sequences or cgMLST profiles efficiently.
- **Input/Output**: Input: FASTA sequences or cgMLST allele profiles (TSV). Output: Distance matrices (TSV).
- **Algorithm**: Uses efficient algorithms for distance calculation including Hamming distance, Jaccard index, etc.
- **Key Features**: Fast distance calculation, supports cgMLST profiles, multiple distance metrics, parallel processing, large dataset support.
- **Installation**: `conda install -c bioconda distle`

## Pitfalls

- **Input Format**: Requires FASTA or cgMLST allele profiles.
- **Profile Quality**: cgMLST profiles must be properly formatted.
- **Memory Usage**: Large datasets may require significant memory.
- **Distance Metric**: Choosing appropriate distance metric is important.
- **Sequence Length**: Variable sequence lengths may affect distance calculation.

## Examples

### Calculate distance matrix from profiles
**Args:** `distle --input profiles.tsv --output distances.tsv`
**Explanation:** Calculates distance matrix from cgMLST profiles.

### From FASTA sequences
**Args:** `distle --input sequences.fa --output distances.tsv --fasta`
**Explanation:** Calculate distances from FASTA sequences.

### With specific metric
**Args:** `distle --input profiles.tsv --output distances.tsv --metric hamming`
**Explanation:** Use Hamming distance metric.

### Parallel processing
**Args:** `distle --input profiles.tsv --output distances.tsv --threads 8`
**Explanation:** Use multiple threads for parallel computation.

### Generate tree
**Args:** `distle --input profiles.tsv --output distances.tsv --tree tree.nwk`
**Explanation:** Generate phylogenetic tree from distance matrix.