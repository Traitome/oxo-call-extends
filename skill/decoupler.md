---
name: decoupler
category: utility
description: Ensemble of methods to infer biological activities from omics data.
tags: [decoupler, utility, omics, pathway-analysis, activity-scoring]
author: oxo-call-community
source_url: "https://github.com/saezlab/decoupler-py"
---

## Concepts

- **Tool Overview**: decoupler (v1.5.0+) is a Python package providing an ensemble of methods to infer biological activities from omics data. It integrates multiple statistical approaches for pathway and gene set enrichment analysis.
- **Core Function**: Infers biological activities (pathway activation, transcription factor binding, etc.) from gene expression, proteomics, or metabolomics data using multiple complementary methods.
- **Input/Output**: Input: Omics matrix (genes x samples), prior knowledge networks (e.g., pathways, TF-targets). Output: Activity scores, significance estimates, visualization plots.
- **Algorithm**: Implements multiple methods including weighted mean, z-score, enrichment analysis, and machine learning-based approaches for activity inference.
- **Key Features**: Multi-method ensemble, supports various omics types, comprehensive prior knowledge integration, visualization tools, modular design.
- **Installation**: `conda install -c bioconda decoupler`

## Pitfalls

- **Prior Knowledge Quality**: Results depend on pathway/network quality.
- **Method Selection**: Different methods may give different results.
- **Data Normalization**: Requires proper data normalization.
- **Missing Data**: May handle missing values differently.
- **Computational Resources**: Some methods may be computationally intensive.

## Examples

### Infer pathway activities
**Args:** `decoupler -i expression.csv -p pathways.gmt -o activities.csv`
**Explanation:** Infer pathway activities from gene expression data.

### Use multiple methods
**Args:** `decoupler -i expression.csv -p pathways.gmt --methods wmean zscore -o activities.csv`
**Explanation:** Combine results from weighted mean and z-score methods.

### Visualize results
**Args:** `decoupler -i expression.csv -p pathways.gmt -o activities.csv --plot`
**Explanation:** Generate heatmap of pathway activities.