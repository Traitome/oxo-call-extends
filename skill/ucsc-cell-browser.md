---
name: ucsc-cell-browser
category: visualization
description: UCSC Cell Browser - Tool for visualizing single-cell data.
tags: [ucsc-cell-browser, ucsc, single-cell, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC Cell Browser - A tool for visualizing and exploring single-cell RNA-seq data.
- **Core Function**: Creates interactive visualizations of cell populations.
- **Input**: Single-cell expression data, metadata.
- **Output**: Interactive web-based visualization.
- **Installation**: Part of UCSC utilities
- **Use Case**: Single-cell analysis, cell type identification, data exploration.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Data Format**: Requires specific input format.

## Examples

### Create cell browser
**Args:** `cellBrowser create -i expression.txt -o browser/`
**Explanation:** Create single-cell browser visualization.

### With metadata
**Args:** `cellBrowser create -i expression.txt -m metadata.txt -o browser/`
**Explanation:** Create browser with cell metadata.
