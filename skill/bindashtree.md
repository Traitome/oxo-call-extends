---
name: bindashtree
category: population-genomics
description: Ultra-fast genome phylogenetic tree construction via Binwise Densified MinHash
tags: [phylogeny, tree, minhash, genome-distance]
author: oxo-call-community
source_url: "https://github.com/jianshu93/bindashtree"
---

## Concepts
- **Tool Overview**: bindashtree constructs genome phylogenetic trees using Binwise Densified MinHash and Rapid Neighbor-Joining. It builds trees from genome distance matrices efficiently.
- **Algorithm**: Uses densified MinHash for accurate distance estimation, then applies rapid neighbor-joining for tree construction.
- **Performance**: Designed for ultra-fast tree building from large genome collections.
- **Applications**: Phylogenetic analysis, genome clustering, evolutionary studies.

## Pitfalls
- **Distance Accuracy**: MinHash-based distances are approximations; may differ from alignment-based distances.
- **Tree Quality**: Rapid neighbor-joining may produce different topologies than more sophisticated methods.
- **Outgroup**: Consider adding an outgroup for proper tree rooting.

## Examples
### Build phylogenetic tree
**Args:** `bindashtree -i distance_matrix.tsv -o tree.nwk`
**Explanation:** Constructs a phylogenetic tree from distance matrix.

### Build with bootstrap
**Args:** `bindashtree -i distances.tsv -b 100 -o tree_with_bootstrap.nwk`
**Explanation:** Builds tree with 100 bootstrap replicates for branch support.
