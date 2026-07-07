---
name: teexpo
category: analysis
description: TE-ExPo - Transposable Element Expression Portal for analyzing and visualizing TE expression data.
tags: [teexpo, transposable-element, expression, portal, visualization, te-expression]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/te-expo"
---

## Concepts

- **Tool Overview**: TE-ExPo (Transposable Element Expression Portal) - A web-based portal for analyzing and visualizing transposable element expression from RNA-seq datasets.
- **Core Function**: Provides interactive visualization and statistical analysis of TE-derived transcription across samples and conditions.
- **Input**: Expression count matrices (TE-Count output) or raw RNA-seq data.
- **Output**: Interactive visualizations, differential expression results, and downloadable reports.
- **Installation**: Web-based tool available at te-expo website, or deploy locally via Docker.
- **Use Case**: Exploring TE expression dynamics in development, disease, and evolutionary studies.

## Pitfalls

- **Web Access**: Requires internet access for the web portal or significant resources for local deployment.
- **Data Format**: Requires processed TE expression data in specific format.

## Examples

### Upload expression data
**Args:** Upload TE-Count output via web interface at te-expo website.
**Explanation:** Standard web interface workflow for uploading and analyzing TE expression data.

### Differential expression analysis
**Args:** Select conditions and run differential expression via TE-ExPo web interface.
**Explanation:** Interactive analysis to identify TEs with condition-specific expression.
