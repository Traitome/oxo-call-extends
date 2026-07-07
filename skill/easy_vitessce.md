---
name: easy_vitessce
category: visualization
description: "A package to easily use Vitessce to create interactive plots for single-cell data"
tags: [easy_vitessce, visualization, single-cell, Vitessce, interactive-plots]
author: oxo-call-community
source_url: "https://github.com/vitessce/easy_vitessce/"
---

## Concepts

- **Tool Overview**: easy-vitessce is a Python package that simplifies creating interactive visualizations for single-cell omics data using Vitessce.
- **Core Function**: Provides a high-level API to create interactive dashboards for exploring single-cell RNA-seq, ATAC-seq, and spatial transcriptomics data.
- **Input/Output**: Input: AnnData objects, Seurat objects, or various single-cell data formats. Output: Interactive Vitessce dashboards.
- **Algorithm**: Leverages Vitessce visualization framework with WebGL for high-performance interactive rendering.
- **Key Features**: Simplified API, support for multiple data types, interactive exploration, sharing capabilities, Jupyter notebook integration.
- **Installation**: `pip install easy-vitessce`

## Pitfalls

- **Data Size**: Large datasets may require downsampling for smooth visualization.
- **Browser Requirements**: Requires modern web browser with WebGL support.
- **Memory Usage**: Loading large datasets can be memory-intensive.
- **Version Compatibility**: API may change between versions.
- **Network Access**: Some features require internet access for CDN resources.

## Examples

### Basic visualization
**Args:** `import easy_vitessce; easy_vitessce.widget(adata).show()`
**Explanation:** Creates interactive visualization from AnnData object.

### With multiple datasets
**Args:** `easy_vitessce.widget([adata1, adata2], names=["Dataset1", "Dataset2"]).show()`
**Explanation:** Visualizes multiple datasets in a single dashboard.

### Custom layout
**Args:** `easy_vitessce.widget(adata, layout="circular").show()`
**Explanation:** Uses circular layout for visualization.

### Export to HTML
**Args:** `easy_vitessce.widget(adata).export("viz.html")`
**Explanation:** Exports visualization to standalone HTML file.

### With cell annotations
**Args:** `easy_vitessce.widget(adata, color_by="cell_type").show()`
**Explanation:** Colors cells by cell type annotation.