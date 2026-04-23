---
name: baltic
category: utility
description: BaltiC - Lightweight package for analyzing, manipulating and visualizing annotated phylogenetic trees
tags: [phylogenetics, tree-visualization, tree-manipulation, python]
author: oxo-call-community
source_url: "https://github.com/evogytis/baltic"
---

## Concepts

- **Tool Overview**: BaltiC is a Python package for parsing, manipulating, and visualizing annotated phylogenetic trees, designed for evolutionary analysis.

- **Tree Parsing**: Parses various tree file formats including Newick, Nexus, and BEAST output.

- **Annotation Support**: Handles rich metadata annotations on trees, including branch attributes and node features.

- **Visualization**: Creates publication-quality tree visualizations with customizable styling.

- **Tree Manipulation**: Supports tree pruning, rooting, ladderizing, and other common operations.

## Pitfalls

- **Large Trees**: Very large trees (>10,000 tips) may be slow to render. Consider subsampling.

- **Memory Usage**: Complex annotations increase memory usage. Monitor for large datasets.

- **Format Compatibility**: Some annotation formats may not be fully supported. Verify parsing results.

## Examples

### Parse tree file
**Args:** `python -c "import baltic as bt; tree = bt.loadNewick('tree.nwk'); print(len(tree.Objects))"`
**Explanation:** Loads Newick tree and counts number of nodes.

### Visualize tree
**Args:** `python -c "import baltic as bt; tree = bt.loadNexus('beast.tree'); bt.plotTree(tree, 'tree.pdf')"`
**Explanation:** Creates PDF visualization of BEAST tree.

### Prune tree
**Args:** `python -c "import baltic as bt; tree = bt.loadNewick('tree.nwk'); pruned = bt.subtree(tree, tips=['A','B','C'])"`
**Explanation:** Extracts subtree containing only specified tips.

### Root tree
**Args:** `python -c "import baltic as bt; tree = bt.loadNewick('tree.nwk'); bt.reroot(tree, 'outgroup')"`
**Explanation:** Reroots tree using specified outgroup.
