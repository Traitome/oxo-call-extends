---
name: tissuumaps
category: visualization
description: TissUUmaps - Interactive visualization tool for spatial transcriptomics data.
tags: [tissuumaps, spatial-transcriptomics, visualization, spatial-data, rna-seq]
author: oxo-call-community
source_url: "https://github.com/TissUUmaps/TissUUmaps"
---

## Concepts

- **Tool Overview**: TissUUmaps - An interactive visualization tool for exploring spatial transcriptomics data.
- **Core Function**: Provides interactive visualization of gene expression in spatial context, enabling exploration of tissue architecture.
- **Input**: Spatial transcriptomics data (Visium, Slide-seq, etc.), gene expression matrices.
- **Output**: Interactive web-based visualization, publication-quality figures.
- **Installation**: `pip install tissuumaps` or use web version
- **Use Case**: Spatial transcriptomics analysis, tissue architecture exploration, data sharing.

## Pitfalls

- **Data Size**: Large spatial datasets may require subsampling for visualization.
- **Browser Requirements**: Web-based visualization requires modern browser.

## Examples

### Launch visualization
**Args:** `tissuumaps --input spatial_data.h5ad --output visualization/`
**Explanation:** Launch TissUUmaps visualization for spatial transcriptomics data.

### Export figure
**Args:** `tissuumaps export -i data.h5ad -g gene_name -o figure.png`
**Explanation:** Export publication-quality figure of gene expression.
