---
name: treeswift
category: analysis
description: TreeSwift - Tool for efficient phylogenetic tree manipulation.
tags: [treeswift, phylogenetic-tree, tree-manipulation, bioinformatics, python]
author: oxo-call-community
source_url: "https://github.com/niemasd/TreeSwift"
---

## Concepts

- **Tool Overview**: TreeSwift - A fast Python library for phylogenetic tree manipulation and analysis.
- **Core Function**: Provides efficient tree parsing, manipulation, and analysis operations.
- **Input**: Phylogenetic trees (Newick/Nexus format).
- **Output**: Modified trees, tree statistics, analysis results.
- **Installation**: `pip install treeswift`
- **Use Case**: Tree manipulation, phylogenetic analysis, bioinformatics pipelines.

## Pitfalls

- **Python Dependency**: Requires Python knowledge for full functionality.
- **Large Trees**: Memory considerations for very large trees.

## Examples

### Parse and manipulate tree
**Args:** `python -c "from treeswift import read_tree; t = read_tree('tree.nwk'); print(t)"`
**Explanation:** Parse and print tree using TreeSwift.

### Tree statistics
**Args:** `python -c "from treeswift import read_tree; t = read_tree('tree.nwk'); print(t.distance_matrix())"`
**Explanation:** Calculate distance matrix from tree.
