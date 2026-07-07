---
name: shiptv
category: population-genomics
description: shiptv - Interactive phylogenetic tree visualization
tags: ["shiptv", "population-genomics", "phylogeny", "visualization"]
author: oxo-call-community
source_url: "https://github.com/peterk87/shiptv"
---

## Concepts

- **Tool Overview**: shiptv (v0.4.1) generates interactive phylogenetic tree visualizations.
- **Core Function**: Creates standalone HTML files with interactive trees.
- **Algorithm**: Uses PhyloCanvas for interactive visualization.
- **Input/Output**: Accepts tree files and produces HTML visualizations.
- **Phylogenetic Visualization**: Focuses on interactive tree display.
- **Applications**: Phylogenetics, evolutionary biology, and data visualization.

## Pitfalls

- **Memory Usage**: High memory requirements for large trees.
- **Input Format**: Requires correct tree format (Newick, Nexus).
- **Parameter Tuning**: Requires careful adjustment for optimal visualization.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.
- **Browser Compatibility**: May require modern web browser.

## Examples

### Generate tree visualization
**Args:** `shiptv -i tree.newick -o tree.html`
**Explanation:** `-i` input tree; `-o` output HTML.

### With metadata
**Args:** `shiptv -i tree.newick -m metadata.tsv -o tree.html`
**Explanation:** `-m` metadata file for coloring.

### Verbose logging
**Args:** `shiptv -v -i tree.newick -o tree.html`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shiptv --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shiptv --version`
**Explanation:** Shows current version.

### Custom colors
**Args:** `shiptv -i tree.newick -c colors.txt -o tree.html`
**Explanation:** `-c` custom color configuration.

### Title
**Args:** `shiptv -i tree.newick -t "My Tree" -o tree.html`
**Explanation:** `-t` sets tree title.