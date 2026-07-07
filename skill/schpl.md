---
name: schpl
category: single-cell
description: scHPL - Hierarchical progressive learning pipeline for single-cell RNA-sequencing datasets
tags: ["schpl", "single-cell", "RNA-seq", "classification"]
author: oxo-call-community
source_url: "https://github.com/lcmmichielsen/scHPL"
---

## Concepts

- **Tool Overview**: scHPL (v1.0.5) is a hierarchical progressive learning pipeline for single-cell RNA-sequencing datasets.
- **Core Function**: Performs hierarchical cell type classification using progressive learning.
- **Algorithm**: Uses hierarchical classification approach with progressive learning strategy.
- **Input/Output**: Accepts gene expression data and produces cell type annotations.
- **Hierarchical Classification**: Organizes cell types in a hierarchical structure.
- **Applications**: Single-cell RNA-seq analysis, cell type identification, and tissue classification.

## Pitfalls

- **Training Data**: Requires high-quality training data for accurate classification.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Hierarchy Design**: Hierarchy design affects classification performance.
- **Biological Variation**: May struggle with highly variable biological data.

## Examples

### Basic classification
**Args:** `schpl classify -i query.h5ad -t training.h5ad -o annotations.csv`
**Explanation:** `-i` query data; `-t` training data; `-o` cell type annotations.

### Train model
**Args:** `schpl train -i training.h5ad -o model.pt`
**Explanation:** Trains hierarchical classification model.

### Hierarchical analysis
**Args:** `schpl hierarchy -i data.h5ad -o hierarchy.txt`
**Explanation:** Analyzes and visualizes cell type hierarchy.

### Cross-validation
**Args:** `schpl cv -i data.h5ad -k 5 -o results.csv`
**Explanation:** `-k 5` performs 5-fold cross-validation.

### Verbose logging
**Args:** `schpl classify -i query.h5ad -t training.h5ad -v -o annotations.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Confidence threshold
**Args:** `schpl classify -i query.h5ad -t training.h5ad -c 0.8 -o annotations.csv`
**Explanation:** `-c 0.8` requires minimum confidence of 0.8.

### Output probabilities
**Args:** `schpl classify -i query.h5ad -t training.h5ad --probabilities -o predictions.csv`
**Explanation:** `--probabilities` outputs classification probabilities.