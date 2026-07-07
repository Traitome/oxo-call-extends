---
name: jclusterfunk
category: hpc
description: A command line tool with functions for phylogenetic tree manipulation and analysis.
tags: [jclusterfunk, hpc, phylogenetics, tree, clustering]
author: oxo-call-community
source_url: "https://github.com/snake-flu/jclusterfunk"
---

## Concepts

- **Tool Overview**: jclusterfunk (v0.0.25) - A command-line tool for manipulating and analyzing phylogenetic trees with various clustering functions.
- **Tree Manipulation**: Provides functions for modifying and annotating phylogenetic trees.
- **Clustering Analysis**: Performs clustering analysis on tree structures.
- **Tree Comparison**: Compares multiple phylogenetic trees.
- **Bootstrap Analysis**: Analyzes bootstrap support values.
- **Visualization Support**: Generates output for tree visualization tools.

## Pitfalls

- **Tree Format Compatibility**: May not support all tree formats.
- **Large Trees**: Processing very large trees requires significant memory.
- **Bootstrap Thresholds**: Choosing appropriate bootstrap thresholds requires care.
- **Topology Differences**: Different tree topologies can affect clustering results.
- **Branch Lengths**: Ignoring branch lengths can affect clustering.
- **Outgroup Selection**: Outgroup selection affects rooting and clustering.

## Examples

### Cluster tree by bootstrap support
**Args:** `jclusterfunk cluster --tree tree.nwk --bootstrap 0.7`
**Explanation:** Clusters tree nodes with bootstrap support ≥70%.

### Compare two trees
**Args:** `jclusterfunk compare --tree1 tree1.nwk --tree2 tree2.nwk`
**Explanation:** Compares topology of two phylogenetic trees.

### Root tree
**Args:** `jclusterfunk root --tree tree.nwk --outgroup speciesA`
**Explanation:** Roots tree using specified outgroup.

### Extract subtree
**Args:** `jclusterfunk extract --tree tree.nwk --species species1 species2 species3 --out subtree.nwk`
**Explanation:** Extracts subtree containing specified species.

### Prune tree
**Args:** `jclusterfunk prune --tree tree.nwk --remove species_to_remove.txt`
**Explanation:** Removes specified species from tree.

### Generate report
**Args:** `jclusterfunk report --tree tree.nwk --out report.txt`
**Explanation:** Generates detailed tree analysis report.