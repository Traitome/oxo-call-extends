---
name: scvi-tools
category: single-cell
description: scvi-tools - Deep probabilistic analysis of single-cell omics data
tags: ["scvi-tools", "single-cell", "deep-learning", "probabilistic-modeling"]
author: oxo-call-community
source_url: "https://docs.scvi-tools.org/en/stable/"
---

## Concepts

- **Tool Overview**: scvi-tools (v0.14.5) provides deep probabilistic analysis of single-cell omics data.
- **Core Function**: Implements various deep learning models for single-cell data analysis.
- **Algorithm**: Uses variational autoencoders and other deep learning techniques.
- **Input/Output**: Accepts AnnData objects and produces analyzed results.
- **Multi-Omics**: Supports integration of multiple omics data types.
- **Applications**: Dimensionality reduction, batch correction, cell type identification, and integration.

## Pitfalls

- **Computational Resources**: Requires significant compute resources, especially GPU.
- **Memory Usage**: High memory requirements for large datasets.
- **Training Time**: May require long training times.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **GPU Availability**: Performance benefits significantly from GPU acceleration.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Import and setup
**Args:** `import scvi; scvi.model.SCVI.setup_anndata(adata)`
**Explanation:** Sets up AnnData for SCVI.

### Initialize model
**Args:** `model = scvi.model.SCVI(adata)`
**Explanation:** Initializes SCVI model.

### Train model
**Args:** `model.train()`
**Explanation:** Trains the model on data.

### Get latent representation
**Args:** `latent = model.get_latent_representation()`
**Explanation:** Extracts latent representation.

### Save model
**Args:** `model.save('scvi_model/', overwrite=True)`
**Explanation:** Saves trained model.

### Load model
**Args:** `model = scvi.model.SCVI.load('scvi_model/', adata=adata)`
**Explanation:** Loads previously saved model.

### Differential expression
**Args:** `de_results = model.differential_expression(groupby='cell_type')`
**Explanation:** Performs differential expression analysis.