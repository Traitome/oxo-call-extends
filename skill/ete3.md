---
name: ete3
category: programming
description: "A Python framework for the analysis and visualization of trees"
tags: [ete3, programming, phylogenetics, tree-visualization, evolutionary-analysis]
author: oxo-call-community
source_url: "http://etetoolkit.org/"
---

## Concepts

- **Tool Overview**: ETE3 (Environment for Tree Exploration version 3) is a comprehensive Python framework for phylogenetic tree analysis, manipulation, and visualization.
- **Core Function**: Provides a robust API for reading, writing, manipulating, and visualizing phylogenetic trees in various formats.
- **Input/Output**: Input: Phylogenetic trees (Newick, Nexus, PhyloXML). Output: Modified trees, visualizations (PNG/PDF/SVG), statistical analyses.
- **Algorithm**: Implements tree traversal algorithms, distance calculations, and visualization rendering engines.
- **Key Features**: Tree manipulation, interactive visualization, distance matrix calculation, bootstrap support analysis, tree comparison, plugin system.
- **Installation**: `conda install -c bioconda ete3`

## Pitfalls

- **Memory Usage**: Large trees may require significant memory.
- **Format Compatibility**: Some tree formats may not be fully supported.
- **Visualization**: Complex trees may produce cluttered visualizations.
- **Version Compatibility**: API changes between versions may break existing code.
- **Tree Quality**: Analysis results depend on tree quality and support values.

## Examples

### Load and print tree
**Args:** `python -c "from ete3 import Tree; t = Tree('tree.nwk'); print(t)"`
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