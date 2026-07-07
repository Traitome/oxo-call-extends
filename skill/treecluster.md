---
name: treecluster
category: analysis
description: TreeCluster - Tool for clustering phylogenetic trees.
tags: [treecluster, phylogenetic-tree, clustering, phylogenetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/treecluster"
---

## Concepts

- **Tool Overview**: TreeCluster - A tool for clustering sequences based on phylogenetic tree topology.
- **Core Function**: Identifies clusters within phylogenetic trees using various clustering methods.
- **Input**: Phylogenetic tree (Newick format), sequence data.
- **Output**: Cluster assignments, cluster statistics, visualization data.
- **Installation**: `pip install treecluster` or `conda install -c bioconda treecluster`
- **Use Case**: Population genetics, viral evolution, sequence classification.

## Pitfalls

- **Tree Quality**: Clustering results depend on tree quality.
- **Parameter Selection**: Requires careful parameter tuning for optimal results.

## Examples

### Cluster tree
**Args:** `treecluster -i tree.nwk -o clusters.txt`
**Explanation:** Identify clusters in phylogenetic tree.

### With distance threshold
**Args:** `treecluster -i tree.nwk -d 0.05 -o clusters.txt`
**Explanation:** Cluster with specific distance threshold.
