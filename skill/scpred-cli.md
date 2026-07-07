---
name: scpred-cli
category: single-cell
description: scpred-cli - Command-line wrappers for the scPred package
tags: ["scpred-cli", "single-cell", "cell-type-prediction", "annotation"]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/scPred-cli"
---

## Concepts

- **Tool Overview**: scpred-cli (v0.1.0) provides command-line wrappers for the scPred package.
- **Core Function**: Predicts cell types from single-cell RNA-seq data using machine learning.
- **Algorithm**: Uses machine learning classifiers trained on reference datasets.
- **Input/Output**: Accepts AnnData objects and produces cell type predictions.
- **Transfer Learning**: Enables transfer learning for cell type annotation.
- **Applications**: Single-cell RNA-seq analysis, cell type identification, and data integration.

## Pitfalls

- **Reference Quality**: Results depend on reference dataset quality.
- **Batch Effects**: May be affected by batch effects.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Algorithm Selection**: Choosing the right algorithm requires understanding of data characteristics.

## Examples

### Train model
**Args:** `scpred-cli train -i reference.h5ad -c cell_type -o model.pkl`
**Explanation:** `-i` reference data; `-c` cell type column; `-o` output model.

### Predict cell types
**Args:** `scpred-cli predict -i query.h5ad -m model.pkl -o predictions.csv`
**Explanation:** `-i` query data; `-m` model file; `-o` predictions.

### Evaluate model
**Args:** `scpred-cli evaluate -i test.h5ad -m model.pkl -o metrics.csv`
**Explanation:** Evaluates model performance on test data.

### Feature selection
**Args:** `scpred-cli select-features -i data.h5ad -c cell_type -n 500 -o features.txt`
**Explanation:** `-n 500` selects top 500 features.

### Cross-validation
**Args:** `scpred-cli cv -i data.h5ad -c cell_type -k 5 -o results.csv`
**Explanation:** `-k 5` performs 5-fold cross-validation.

### Verbose logging
**Args:** `scpred-cli predict -i query.h5ad -m model.pkl -v -o predictions.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Batch prediction
**Args:** `scpred-cli batch -i queries/ -m model.pkl -o results/`
**Explanation:** Processes multiple query datasets.