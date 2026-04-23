---
name: calour
category: metagenomics
description: Exploratory and interactive microbiome analyses based on heatmaps
tags: [calour, microbiome, heatmap, visualization, interactive]
author: oxo-call-community
source_url: "https://github.com/biocore/calour"
---

## Concepts

- **Tool Overview**: Calour is a Python package for interactive microbiome analysis using heatmaps.
- **Core Function**: Visualizes and explores microbiome data interactively.
- **Input**: OTU tables, BIOM files, or abundance matrices.
- **Output**: Interactive heatmaps and statistical analysis results.
- **Features**: Database integration, differential abundance testing, and clustering.
- **Installation**: Install via bioconda: `conda install -c bioconda calour`

## Pitfalls

- **Python Only**: Python library with Jupyter notebook interface.
- **Data Format**: Requires properly formatted abundance tables.
- **Memory Usage**: Large datasets require significant memory for interactive visualization.

## Examples

### Load and visualize microbiome data
**Args:** `python -c "import calour as ca; exp = ca.read_amplicon('data.biom'); exp.plot_sample()"`
**Explanation:** Loads BIOM file and creates interactive heatmap visualization.

### Differential abundance analysis
**Args:** `python -c "import calour as ca; exp = ca.read_amplicon('data.biom'); exp.diff_abundance('group')"`
**Explanation:** Performs differential abundance testing between groups.

### Export heatmap
**Args:** `python -c "import calour as ca; exp = ca.read_amplicon('data.biom'); exp.plot_sample(savefig='heatmap.pdf')"`
**Explanation:** Saves heatmap visualization to PDF file.
