---
name: treesap
category: visualization
description: TreeSap - Tool for interactive phylogenetic tree visualization.
tags: [treesap, phylogenetic-tree, visualization, interactive, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/treesap"
---

## Concepts

- **Tool Overview**: TreeSap - A tool for interactive visualization and exploration of phylogenetic trees.
- **Core Function**: Provides interactive tree viewing with zooming, panning, and annotation features.
- **Input**: Phylogenetic tree (Newick format), annotation files.
- **Output**: Interactive tree visualization, exportable images, tree statistics.
- **Installation**: `pip install treesap` or `conda install -c bioconda treesap`
- **Use Case**: Tree exploration, data presentation, phylogenetic analysis.

## Pitfalls

- **Memory**: Large trees may require significant memory.
- **Browser**: Requires web browser for interactive features.

## Examples

### View tree
**Args:** `treesap -i tree.nwk`
**Explanation:** Launch interactive tree viewer.

### Export visualization
**Args:** `treesap -i tree.nwk -o tree.html`
**Explanation:** Export interactive tree visualization to HTML.
