---
name: cellxgene
category: visualization
description: Web application for exploration of large-scale scRNA-seq datasets
tags: [cellxgene, single-cell, visualization, web-app, scrna-seq, exploration]
author: oxo-call-community
source_url: "https://github.com/chanzuckerberg/cellxgene"
---

## Concepts

- **Tool Overview**: cellxgene is an interactive web application for exploring and visualizing single-cell RNA-seq datasets.
- **Core Function**: Provides interactive visualization of scRNA-seq data with cell clustering, gene expression, and metadata exploration.
- **Features**: Interactive UMAP/t-SNE plots, gene expression heatmaps, cell type annotation, and differential expression analysis.
- **Input**: AnnData (.h5ad) files with preprocessed scRNA-seq data.
- **Output**: Interactive web interface for data exploration.
- **Application**: Visual exploration and analysis of single-cell transcriptomic data.
- **Installation**: Install via bioconda: `conda install -c bioconda cellxgene`

## Pitfalls

- **Data Size**: Large datasets may require significant memory and loading time.
- **Preprocessing**: Data must be preprocessed (normalized, clustered) before visualization.
- **Browser Compatibility**: Best viewed in modern browsers (Chrome, Firefox).
- **Network Access**: Requires network access for web interface.

## Examples

### Launch cellxgene with local data
**Args:** `cellxgene launch data.h5ad --host 0.0.0.0 --port 5005`
**Explanation:** Launches cellxgene web server with specified data file.

### Launch with multiple datasets
**Args:** `cellxgene launch dataset1.h5ad dataset2.h5ad --host 0.0.0.0`
**Explanation:** Launches cellxgene with multiple datasets for comparison.

### Specify custom port
**Args:** `cellxgene launch data.h5ad --port 8080`
**Explanation:** Starts cellxgene on port 8080 instead of default.

### Display help
**Args:** `cellxgene --help`
**Explanation:** Shows all available commands and options.