---
name: gefast
category: clustering
description: Clustering tool using Swarm's clustering strategy and Pass-Join's segment filter for fast sequence clustering.
tags: [gefast, clustering, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/romueller/gefast"
---

## Concepts
- **Sequence Clustering**: Clusters biological sequences efficiently.
- **Swarm Algorithm**: Uses Swarm's clustering strategy for sensitive clustering.
- **Pass-Join Filter**: Implements Pass-Join's segment filter for speed.
- **OTU Clustering**: Suitable for OTU (Operational Taxonomic Unit) clustering.
- **High Throughput**: Designed for large-scale sequence data.

## Pitfalls
- **Memory Usage**: May require significant memory for large datasets.
- **Parameter Tuning**: Requires careful parameter adjustment for optimal results.
- **Sequence Length**: Performance may vary with sequence length.
- **Similarity Threshold**: Threshold selection affects clustering results.
- **Output Size**: Large clusters can generate massive output files.

## Examples
### Cluster sequences
**Args:** `gefast -i sequences.fasta -o clusters.txt`
**Explanation:** Clusters sequences using default parameters.

### With custom similarity threshold
**Args:** `gefast -i sequences.fasta -o clusters.txt -t 0.97`
**Explanation:** Clusters sequences with 97% similarity threshold.

### Parallel clustering
**Args:** `gefast -i sequences.fasta -o clusters.txt -p 8`
**Explanation:** Uses 8 threads for parallel clustering.

### Generate OTU table
**Args:** `gefast -i sequences.fasta -o otu_table.txt -f otu`
**Explanation:** Generates OTU table from clustered sequences.

### Filter by cluster size
**Args:** `gefast -i sequences.fasta -o clusters.txt -m 10`
**Explanation:** Filters out clusters with fewer than 10 sequences.