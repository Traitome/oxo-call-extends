---
name: scaden
category: single-cell
description: Cell type deconvolution using single cell reference data
tags: ["scaden", "single-cell", "deconvolution", "cell-type"]
author: oxo-call-community
source_url: "https://github.com/KevinMenden/scaden"
---

## Concepts

- **Tool Overview**: Scaden (v1.1.2) is a tool for cell type deconvolution using single-cell RNA-seq reference data to infer cell type proportions in bulk RNA-seq samples.
- **Core Function**: Uses machine learning models trained on single-cell data to estimate cell type composition from bulk transcriptomics.
- **Algorithm**: Implements neural network-based deconvolution with transfer learning from single-cell reference data.
- **Input/Output**: Accepts bulk RNA-seq expression matrices and single-cell reference data, produces cell type proportion estimates.
- **Reference Building**: Can build reference signatures from single-cell datasets.
- **Applications**: Bulk RNA-seq cell type composition analysis, tissue heterogeneity studies, and disease characterization.

## Pitfalls

- **Reference Quality**: Results depend heavily on reference dataset quality and relevance.
- **Cell Type Overlap**: May struggle with highly similar cell types.
- **Batch Effects**: Sensitive to batch effects between reference and target data.
- **Computational Resources**: Training models requires significant compute resources.
- **Memory Usage**: High memory requirements for large reference datasets.
- **Normalization**: Requires proper normalization between reference and target data.

## Examples

### Train model and deconvolve
**Args:** `scaden train -r reference.h5ad -t target.csv -o results/`
**Explanation:** `-r` reference single-cell data; `-t` target bulk data; `-o` output directory.

### Deconvolve with pre-trained model
**Args:** `scaden predict -m model.h5 -t target.csv -o predictions.csv`
**Explanation:** `-m` pre-trained model; `-t` target bulk data; `-o` predictions output.

### Build reference signature
**Args:** `scaden build -i sc_data.h5ad -o reference_signature.h5ad`
**Explanation:** Builds reference signature matrix from single-cell data.

### Cross-validation
**Args:** `scaden cv -r reference.h5ad -k 5 -o cv_results/`
**Explanation:** `-k 5` performs 5-fold cross-validation on reference data.

### Ensemble prediction
**Args:** `scaden ensemble -m model1.h5 model2.h5 -t target.csv -o predictions.csv`
**Explanation:** Combines predictions from multiple models.

### Feature selection
**Args:** `scaden select -r reference.h5ad -n 1000 -o selected.h5ad`
**Explanation:** `-n 1000` selects top 1000 most informative genes.

### Visualize results
**Args:** `scaden plot -i predictions.csv -o plot.png`
**Explanation:** Generates visualization of cell type proportions.