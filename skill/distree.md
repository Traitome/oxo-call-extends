---
name: distree
category: population-genomics
description: distree - Calculate distances between phylogenetic trees.
tags: [distree, population-genomics, phylogenetics, tree-comparison, distance]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/distree"
---

## Concepts

- **Tool Overview**: distree (v1.0.0+) is a tool for calculating distances between phylogenetic trees.
- **Core Function**: Computes tree distance metrics (Robinson-Foulds, etc.) between phylogenetic trees.
- **Input/Output**: Input: Newick tree files. Output: Pairwise tree distances, distance matrix.
- **Algorithm**: Implements multiple tree distance metrics for comparing tree topologies.
- **Key Features**: Multiple distance metrics, pairwise tree comparison, batch processing, visualization, tree support comparison.
- **Installation**: `conda install -c bioconda distree`

## Pitfalls

- **Input Format**: Requires Newick format tree files.
- **Tree Compatibility**: Trees must have matching leaf sets for comparison.
- **Metric Selection**: Choosing appropriate distance metric is critical.
- **Large Trees**: May be slow for very large trees.
- **Branch Lengths**: Some metrics ignore branch lengths.

## Examples

### Calculate distance between two trees
**Args:** `distree --tree1 tree1.nwk --tree2 tree2.nwk --output distance.txt`
**Explanation:** Calculates distance between two phylogenetic trees.

### Multiple tree comparison
**Args:** `distree --trees trees/*.nwk --output distances.tsv`
**Explanation:** Compute pairwise distances between multiple trees.

### Specific metric
**Args:** `distree --tree1 tree1.nwk --tree2 tree2.nwk --output distance.txt --metric rf`
**Explanation:** Use Robinson-Foulds distance metric.

### Generate distance matrix
**Args:** `distree --trees trees/*.nwk --output distance_matrix.tsv --matrix`
**Explanation:** Generate distance matrix from multiple trees.

### Visualize tree differences
**Args:** `distree --tree1 tree1.nwk --tree2 tree2.nwk --output diff.png --plot`
**Explanation:** Generate visualization of tree differences.