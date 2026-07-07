---
name: spreadgltools
category: visualization
description: SpreadGL - Pathogen dispersal visualization in browser application
tags: [spreadgltools, visualization, pathogen-dispersal, browser, phylogeography]
author: oxo-call-community
source_url: "https://github.com/GuyBaele/SpreadGL"
---

## Concepts

- **Tool Overview**: spreadgltools (v1.1.0) - A pathogen dispersal visualization tool
- **Core Function**: Visualizes pathogen dispersal in high-performance browser application
- **Input/Output**: Accepts phylogenetic and geographic data; outputs interactive visualizations
- **Algorithm**: WebGL-based visualization algorithms
- **Installation**: `conda install -c bioconda spreadgltools`
- **Key Features**: Pathogen visualization, browser-based, high-performance

## Pitfalls

- **Input Requirements**: Requires properly formatted phylogenetic and geographic data
- **Data Quality**: Data quality affects visualization accuracy
- **Browser Compatibility**: Requires WebGL-compatible browser
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Visualization Performance**: Performance depends on dataset size and browser

## Examples

### Display help
**Args:** `spreadgltools --help`
**Explanation:** Shows available options and usage information.

### Basic visualization
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html`
**Explanation:** Create pathogen dispersal visualization.

### With time scale
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html --time-scale`
**Explanation:** Include time scale in visualization.

### With geographic projection
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html --projection mercator`
**Explanation:** Set geographic projection.

### Output detailed results
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html --detailed`
**Explanation:** Output detailed visualization information.

### Output statistics
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html --stats`
**Explanation:** Output visualization statistics.

### Generate report
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html --report`
**Explanation:** Generate visualization report.

### With custom colors
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html --colors custom.json`
**Explanation:** Use custom color scheme.

### With animation
**Args:** `spreadgltools -i phylo_tree.nwk -g locations.tsv -o visualization.html --animate`
**Explanation:** Enable animation in visualization.