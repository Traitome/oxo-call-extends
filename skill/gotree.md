---
name: gotree
category: bioinformatics
description: gotree is a command-line toolkit for manipulating and analyzing phylogenetic trees in various formats.
tags: [gotree, phylogenetics, tree-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/evolbioinfo/gotree"
---

## Concepts

- **Phylogenetic Tree Manipulation**: gotree provides a comprehensive set of commands for manipulating phylogenetic trees.

- **Format Support**: Handles multiple tree formats including Newick, Nexus, and PhyloXML.

- **Tree Operations**: Supports pruning, rooting, unrooting, rerooting, and subtree extraction.

- **Tree Comparison**: Compares trees using various metrics including Robinson-Foulds distance and triplet distance.

- **Visualization**: Generates tree visualizations in various formats including SVG and PNG.

- **Bootstrap Support**: Analyzes bootstrap support values and performs consensus tree generation.

## Pitfalls

- **Format Compatibility**: Ensure input trees are in a supported format. Use conversion commands if needed.

- **Tree Rooting**: Many operations require rooted trees. Check tree rooting status before operations.

- **Branch Lengths**: Some operations may discard branch lengths. Preserve branch lengths when needed.

- **Large Trees**: Processing very large trees may require significant memory. Consider simplifying or subsampling.

- **Bootstrap Values**: Ensure bootstrap values are properly formatted in input trees.

## Examples

### Display tree statistics
**Args:** `gotree stats -i tree.nwk`
**Explanation:** Displays statistics including number of nodes, leaves, and average branch length.

### Root tree
**Args:** `gotree root -i tree.nwk -o rooted.nwk -r "outgroup"`
**Explanation:** Roots the tree using the specified outgroup taxon.

### Prune tree
**Args:** `gotree prune -i tree.nwk -l species_list.txt -o pruned.nwk`
**Explanation:** Removes taxa not in the species list from the tree.

### Compare two trees
**Args:** `gotree compare -i tree1.nwk tree2.nwk`
**Explanation:** Computes Robinson-Foulds distance between two trees.

### Generate consensus tree
**Args:** `gotree consensus -i bootstrap_trees/ -o consensus.nwk`
**Explanation:** Generates a consensus tree from a set of bootstrap replicate trees.

### Draw tree
**Args:** `gotree draw -i tree.nwk -o tree.svg`
**Explanation:** Generates an SVG visualization of the tree.

### Reroot tree
**Args:** `gotree reroot -i tree.nwk -o rerooted.nwk -n "internal_node"`
**Explanation:** Reroots the tree at the specified internal node.