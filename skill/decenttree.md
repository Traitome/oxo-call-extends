---
name: decenttree
category: variant-calling
description: Scalable Neighbour-Joining and related algorithms for phylogenetic tree inference.
tags: [decenttree, variant-calling, phylogenetics, tree-inference, Neighbour-Joining]
author: oxo-call-community
source_url: "https://github.com/iqtree/decenttree"
---

## Concepts

- **Tool Overview**: decenttree (v1.0.0+) is a fast and memory-efficient implementation of distance-based phylogenetic tree construction methods, including Neighbour-Joining and its variants. It is designed for large-scale phylogenetic analyses.
- **Core Function**: Constructs phylogenetic trees from distance matrices using Neighbour-Joining algorithm and related methods, optimized for scalability and memory efficiency.
- **Input/Output**: Input: FASTA sequences or distance matrix. Output: Newick tree file, distance matrix statistics.
- **Algorithm**: Implements Neighbour-Joining algorithm with optimizations for large datasets, including fast distance computation and memory-efficient data structures.
- **Key Features**: Scalable to thousands of taxa, memory-efficient, supports multiple distance metrics, integrates with IQ-TREE.
- **Installation**: `conda install -c bioconda decenttree`

## Pitfalls

- **Distance Metric**: Choice of distance metric affects tree topology.
- **Outgroup Selection**: Requires appropriate outgroup for rooting.
- **Alignment Quality**: Poor alignments produce inaccurate trees.
- **Computational Time**: Very large datasets may require significant time.
- **Memory Usage**: May require careful memory management for very large analyses.

## Examples

### Build tree from sequences
**Args:** `decenttree -i sequences.fasta -o tree.nwk`
**Explanation:** Construct phylogenetic tree from aligned sequences.

### Use specific distance model
**Args:** `decenttree -i sequences.fasta -o tree.nwk -m GTR`
**Explanation:** Use GTR distance model for tree construction.

### Build from distance matrix
**Args:** `decenttree -d distance_matrix.txt -o tree.nwk`
**Explanation:** Construct tree from pre-computed distance matrix.