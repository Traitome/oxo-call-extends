---
name: treemaker
category: utility
description: TreeMaker - Tool for generating phylogenetic tree visualizations.
tags: [treemaker, phylogenetic-tree, visualization, bioinformatics, tree-drawing]
author: oxo-call-community
source_url: "https://github.com/compbio/treemaker"
---

## Concepts

- **Tool Overview**: TreeMaker - A tool for generating publication-quality phylogenetic tree visualizations.
- **Core Function**: Creates tree drawings with customizable styles and annotations.
- **Input**: Phylogenetic tree (Newick format), annotation files.
- **Output**: Tree images (PNG/SVG), publication-ready figures.
- **Installation**: `pip install treemaker` or `conda install -c bioconda treemaker`
- **Use Case**: Phylogenetic visualization, publication figure generation, data presentation.

## Pitfalls

- **Large Trees**: May have issues with very large phylogenetic trees.
- **Customization**: Requires learning curve for advanced customization.

## Examples

### Draw tree
**Args:** `treemaker -i tree.nwk -o tree.png`
**Explanation:** Generate tree visualization from Newick format.

### With annotations
**Args:** `treemaker -i tree.nwk -a annotations.txt -o annotated_tree.png`
**Explanation:** Draw tree with annotations.
