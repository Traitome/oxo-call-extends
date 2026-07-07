---
name: ete2
category: population-genomics
description: "Phylogenetic tree analyses and exploration"
tags: [ete2, population-genomics, phylogenetics, tree-visualization, evolutionary-analysis]
author: oxo-call-community
source_url: "http://etetoolkit.org/"
---

## Concepts

- **Tool Overview**: ETE (Environment for Tree Exploration) is a Python library for phylogenetic tree analysis, manipulation, and visualization.
- **Core Function**: Provides tools for reading, writing, manipulating, and visualizing phylogenetic trees in various formats.
- **Input/Output**: Input: Phylogenetic trees (Newick, Nexus, PhyloXML). Output: Modified trees, visualizations, statistical analyses.
- **Algorithm**: Implements various tree traversal algorithms, distance calculations, and visualization methods.
- **Key Features**: Tree manipulation, visualization, distance matrix calculation, bootstrap support analysis, tree comparison, integration with other tools.
- **Installation**: `conda install -c bioconda ete2`

## Pitfalls

- **Memory Usage**: Large trees may require significant memory.
- **Format Compatibility**: Some tree formats may not be fully supported.
- **Visualization**: Complex trees may produce cluttered visualizations.
- **Version Compatibility**: API may change between versions.
- **Tree Quality**: Analysis results depend on tree quality and support values.

## Examples

### Load and visualize tree
**Args:** `python -c "from ete2 import Tree; t = Tree('tree.nwk'); print(t)"`
**Explanation:** Loads and prints a phylogenetic tree.

### Tree manipulation
**Args:** `python -c "t = Tree('tree.nwk'); t.prune(['A', 'B', 'C'])"`
**Explanation:** Prunes tree to include only specified taxa.

### Calculate distances
**Args:** `python -c "t = Tree('tree.nwk'); print(t.get_distance('A', 'B'))"`
**Explanation:** Calculates distance between two nodes.

### Visualize tree
**Args:** `python -c "t = Tree('tree.nwk'); t.render('tree.png')"`
**Explanation:** Renders tree as PNG image.

### Bootstrap analysis
**Args:** `python -c "t = Tree('tree.nwk'); print(t.get_support())"`
**Explanation:** Extracts bootstrap support values from tree.