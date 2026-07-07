---
name: scvi
category: single-cell
description: scVI - Single-cell Variational Inference
tags: ["scvi", "single-cell", "variational-inference", "deep-learning"]
author: oxo-call-community
source_url: "https://scvi.readthedocs.io"
---

## Concepts

- **Tool Overview**: scVI (v0.6.8) performs single-cell Variational Inference for dimensionality reduction and analysis.
- **Core Function**: Uses deep probabilistic models for single-cell data analysis.
- **Algorithm**: Implements variational autoencoders for unsupervised learning.
- **Input/Output**: Accepts gene expression matrices and produces latent representations.
- **Deep Learning**: Leverages neural networks for complex pattern discovery.
- **Applications**: Dimensionality reduction, batch correction, and cell type identification.

## Pitfalls

- **Computational Resources**: Requires significant compute resources, especially GPU.
- **Memory Usage**: High memory requirements for large datasets.
- **Training Time**: May require long training times.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **GPU Availability**: Performance benefits significantly from GPU acceleration.
- **Overfitting**: May overfit to training data.

## Examples

### Basic analysis
**Args:** `import scvi; model = scvi.SCVI(adata)`
**Explanation:** Initializes SCVI model.

### Train model
**Args:** `model.train()`
**Explanation:** Trains the model on data.

### Get latent representation
**Args:** `latent = model.get_latent_representation()`
**Explanation:** Extracts latent representation.

### Save model
**Args:** `model.save('scvi_model/')`
**Explanation:** Saves trained model.

### Load model
**Args:** `model = scvi.SCVI.load('scvi_model/', adata=adata)`
**Explanation:** Loads previously saved model.

### Batch correction
**Args:** `scvi.data.poisson_gene_selection(adata)`
**Explanation:** Performs gene selection for batch correction.

### Differential expression
**Args:** `de_results = model.differential_expression(groupby='cell_type')`
**Explanation:** Performs differential expression analysis.