---
name: treeswirl
category: visualization
description: TreeSwirl - Tool for animated phylogenetic tree visualization.
tags: [treeswirl, phylogenetic-tree, visualization, animation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/treeswirl"
---

## Concepts

- **Tool Overview**: TreeSwirl - A tool for creating animated phylogenetic tree visualizations.
- **Core Function**: Generates animated visualizations of phylogenetic trees and evolutionary processes.
- **Input**: Phylogenetic tree (Newick format), metadata, evolutionary data.
- **Output**: Animated tree visualizations (GIF/MP4), interactive animations.
- **Installation**: `pip install treeswirl` or `conda install -c bioconda treeswirl`
- **Use Case**: Data presentation, evolutionary visualization, education.

## Pitfalls

- **Performance**: Animation may be slow for large trees.
- **File Size**: Output files may be large.

## Examples

### Create animation
**Args:** `treeswirl -i tree.nwk -o animation.gif`
**Explanation:** Create animated visualization of phylogenetic tree.

### With metadata
**Args:** `treeswirl -i tree.nwk -m metadata.txt -o animated_tree.mp4`
**Explanation:** Create animated tree with metadata overlay.
