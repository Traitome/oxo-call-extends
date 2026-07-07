---
name: mcl
category: hpc
description: Markov Cluster Algorithm for graph clustering and community detection.
tags: [mcl, graph-clustering, community-detection]
author: oxo-call-community
source_url: "https://micans.org/mcl"
---

## Concepts

- **Tool Overview**: MCL performs graph clustering using Markov chain simulation.
- **Core Function**: Identifies clusters in graphs via random walks.
- **Markov Clustering**: Uses inflation parameter to control cluster granularity.
- **Graph Input**: Accepts various graph formats.
- **Scalability**: Handles large graphs efficiently.
- **Installation**: `conda install -c bioconda mcl`

## Pitfalls

- **Parameter Sensitivity**: Inflation parameter affects results significantly.
- **Memory Requirements**: Large graphs require significant memory.
- **Computation Time**: Can be slow for very large graphs.
- **Graph Quality**: Poor graph quality affects clustering.
- **Result Interpretation**: Clusters may require biological interpretation.
- **Convergence**: Requires proper convergence criteria.

## Examples

### Basic clustering
**Args:** `mcl graph.txt -I 2.0 -o clusters.txt`
**Explanation:** Clusters graph with inflation parameter 2.0.

### With different inflation
**Args:** `mcl graph.txt -I 1.4 -o clusters.txt`
**Explanation:** Uses lower inflation for larger clusters.

### Verbose output
**Args:** `mcl graph.txt -I 2.0 -v -o clusters.txt`
**Explanation:** Shows detailed clustering progress.

### Cluster size distribution
**Args:** `mcl graph.txt -I 2.0 --show-size -o clusters.txt`
**Explanation:** Shows cluster size distribution.

### Help documentation
**Args:** `mcl --help`
**Explanation:** Displays available options.
