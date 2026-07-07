---
name: markov_clustering
category: programming
description: This module implements the MCL algorithm in python.
tags: [markov_clustering, programming, MCL, clustering]
author: oxo-call-community
source_url: "https://github.com/GuyAllard/markov_clustering"
---

## Concepts

- **Tool Overview**: markov_clustering v0.0.6 - A Python implementation of the Markov Clustering (MCL) algorithm for graph clustering.
- **Core Function**: Performs graph clustering using the MCL algorithm for community detection.
- **Input/Output**: Input: Graph adjacency matrix, network data; Output: Cluster assignments, community structures.
- **Installation**: `conda install -c bioconda markov_clustering`
- **MCL Algorithm**: Uses Markov chain simulation for graph clustering.
- **Community Detection**: Identifies communities in complex networks.

## Pitfalls

- **Graph Size**: Large graphs require significant memory.
- **Parameter Tuning**: Inflation parameter affects cluster granularity.
- **Convergence**: May require many iterations to converge.
- **Initialization**: Random initialization affects results.
- **Interpretation**: Cluster assignments may be hard to interpret.
- **Computational Time**: Complex graphs may take time to process.

## Examples

### Basic clustering
**Args:** `import markov_clustering as mc; result = mc.run_mcl(matrix)`
**Explanation:** Runs MCL clustering on adjacency matrix.

### With inflation
**Args:** `import markov_clustering as mc; result = mc.run_mcl(matrix, inflation=2.0)`
**Explanation:** Sets inflation parameter to 2.0.

### Get clusters
**Args:** `import markov_clustering as mc; clusters = mc.get_clusters(result)`
**Explanation:** Extracts clusters from MCL result.

### Verbose mode
**Args:** `import markov_clustering as mc; result = mc.run_mcl(matrix, verbose=True)`
**Explanation:** Provides detailed logging during clustering.

### Multiple iterations
**Args:** `import markov_clustering as mc; result = mc.run_mcl(matrix, max_iter=100)`
**Explanation:** Sets maximum iterations to 100.

### Save results
**Args:** `import markov_clustering as mc; mc.save_clusters(clusters, 'clusters.txt')`
**Explanation:** Saves cluster assignments to file.