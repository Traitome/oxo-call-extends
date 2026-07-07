---
name: singlecellnet-cli
category: single-cell
description: singlecellnet-cli - Command-line interface for SingleCellNet
tags: ["singlecellnet-cli", "single-cell", "classification", "python"]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/singlecellnet-cli"
---

## Concepts

- **Tool Overview**: singlecellnet-cli (v0.0.1) provides command-line wrappers for SingleCellNet.
- **Core Function**: Classifies single-cell RNA-seq data using reference datasets.
- **Algorithm**: Uses machine learning for cell type classification.
- **Input/Output**: Accepts gene expression data and produces cell type predictions.
- **Cell Type Classification**: Specialized for single-cell classification.
- **Applications**: Single-cell RNA-seq analysis, cell type identification.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Dependency Issues**: Requires SingleCellNet R package.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on data quality.
- **Version Compatibility**: Early development stage, API may change.
- **Documentation**: Limited documentation available.

## Examples

### Train classifier
**Args:** `singlecellnet-cli train -i training_data.h5ad -o model.pkl`
**Explanation:** `-i` training data; `-o` output model.

### Classify cells
**Args:** `singlecellnet-cli classify -i query.h5ad -m model.pkl -o predictions.csv`
**Explanation:** `-m` trained model; `-o` predictions.

### With markers
**Args:** `singlecellnet-cli train -i training_data.h5ad -g markers.txt -o model.pkl`
**Explanation:** `-g` gene markers file.

### Help command
**Args:** `singlecellnet-cli --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `singlecellnet-cli --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `singlecellnet-cli -v classify -i query.h5ad -m model.pkl -o predictions.csv`
**Explanation:** `-v` verbose output.

### Cross-validation
**Args:** `singlecellnet-cli cv -i data.h5ad -k 5 -o cv_results.csv`
**Explanation:** `-k 5` 5-fold cross-validation.
