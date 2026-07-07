---
name: curlywhirly
category: utility
description: CurlyWhirly is an application for viewing multi-dimensional data with focus on PCA and PCoA outputs
tags: [curlywhirly, utility, visualization, PCA, PCoA, multi-dimensional]
author: oxo-call-community
source_url: "https://ics.hutton.ac.uk/curlywhirly"
---

## Concepts

- **Tool Overview**: curlywhirly (v1.17.08.31+) is a Java application for visualizing multi-dimensional data, with special focus on Principal Component Analysis (PCA) and Principal Coordinate Analysis (PCoA) results.
- **Core Function**: Provides interactive 3D visualization of high-dimensional data projections, allowing users to explore clustering patterns and relationships.
- **Input/Output**: Input: Tab-separated values (TSV) with coordinates and metadata. Output: Interactive visualizations, image exports.
- **Key Features**: 3D scatter plots, color-coded groups, interactive rotation/zooming, export to image formats.
- **Installation**: `conda install -c bioconda curlywhirly`

## Pitfalls

- **Java Requirement**: Requires Java runtime environment (JRE 8+).
- **Input Format**: Strict TSV format required; ensure correct column ordering.
- **Memory Usage**: Large datasets may require increasing Java heap size.
- **Display Requirements**: Requires graphics hardware acceleration for smooth rendering.
- **File Size**: Very large datasets may impact performance; consider downsampling.

## Examples

### Run CurlyWhirly with PCA results
**Args:** `curlywhirly -i pca_results.tsv`
**Explanation:** Load and visualize PCA results interactively.

### Load with group colors
**Args:** `curlywhirly -i data.tsv -g groups.txt`
**Explanation:** Visualize data with groups color-coded based on metadata file.

### Export visualization
**Args:** `curlywhirly -i data.tsv -o plot.png --export`
**Explanation:** Generate and export visualization to PNG image file.
