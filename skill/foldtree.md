---
name: foldtree
category: utility
description: Foldtree creates phylogenetic trees from protein structures using Foldseek.
tags: [foldtree, protein structure, phylogenetics, tree building]
author: oxo-call-community
source_url: "https://github.com/DessimozLab/fold_tree"
---

## Concepts
- **Structure-Based Phylogeny**: Infers evolutionary relationships from 3D protein structures.
- **Foldseek Integration**: Uses Foldseek for structural similarity calculations.
- **Distance Matrix**: Constructs a distance matrix based on structural similarity scores.
- **Tree Construction**: Builds phylogenetic trees using distance-based methods.
- **Visualization Ready**: Outputs trees in formats compatible with visualization tools.

## Pitfalls
- **Structure Quality**: Poorly resolved structures can distort phylogenetic inference.
- **Computational Time**: Processing many structures can be time-consuming.
- **Homology Assumption**: Assumes structural similarity reflects evolutionary relatedness.
- **Outgroup Selection**: Requires careful outgroup selection for rooted trees.
- **Interpretation**: Structural trees may differ from sequence-based trees.

## Examples
### Build tree from structure directory
**Args:** `foldtree build structures/ -o tree.nwk`
**Explanation:** Builds a phylogenetic tree from all structures in a directory.

### Build tree with specific outgroup
**Args:** `foldtree build structures/ -o tree.nwk --outgroup outgroup.pdb`
**Explanation:** Builds a rooted tree using the specified outgroup structure.

### Calculate distance matrix
**Args:** `foldtree dist structures/ -o distances.tsv`
**Explanation:** Computes pairwise structural distances between all structures.

### Build tree with specific method
**Args:** `foldtree build structures/ -o tree.nwk --method nj`
**Explanation:** Builds a tree using neighbor-joining method.

### Compare structure and sequence trees
**Args:** `foldtree compare struct_tree.nwk seq_tree.nwk -o comparison.txt`
**Explanation:** Compares a structure-based tree with a sequence-based tree.