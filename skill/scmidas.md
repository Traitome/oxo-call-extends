---
name: scmidas
category: single-cell
description: scMIDAS - A torch-based integration method for single-cell multi-omic data
tags: ["scmidas", "single-cell", "multi-omic", "integration"]
author: oxo-call-community
source_url: "https://scmidas.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: scMIDAS (v0.1.17) is a torch-based integration method for single-cell multi-omic data.
- **Core Function**: Integrates multiple single-cell omics modalities into a unified representation.
- **Algorithm**: Uses deep learning with PyTorch for multi-omic integration.
- **Input/Output**: Accepts multi-omic data and produces integrated embeddings.
- **Deep Learning**: Leverages neural networks for data integration.
- **Applications**: Single-cell multi-omic integration, data visualization, and cross-modality analysis.

## Pitfalls

- **Computational Resources**: Requires significant compute resources, especially GPU.
- **Training Time**: May require long training times.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Data Quality**: Results depend on input data quality.
- **GPU Availability**: Performance benefits from GPU acceleration.

## Examples

### Basic integration
**Args:** `scmidas integrate -i rna.h5ad atac.h5ad -o integrated.h5ad`
**Explanation:** Integrates RNA and ATAC data.

### Train model
**Args:** `scmidas train -i rna.h5ad atac.h5ad -o model.pt`
**Explanation:** Trains integration model on multi-omic data.

### Load model
**Args:** `scmidas integrate -i rna.h5ad atac.h5ad -m model.pt -o integrated.h5ad`
**Explanation:** Uses pre-trained model for integration.

### Visualization
**Args:** `scmidas plot -i integrated.h5ad -o umap.png`
**Explanation:** Generates UMAP visualization of integrated data.

### Verbose logging
**Args:** `scmidas integrate -i rna.h5ad atac.h5ad -v -o integrated.h5ad`
**Explanation:** `-v` enables verbose output for debugging.

### Batch correction
**Args:** `scmidas integrate -i rna.h5ad atac.h5ad --batch-correct -o integrated.h5ad`
**Explanation:** `--batch-correct` applies batch correction.

### Cross-validation
**Args:** `scmidas cv -i rna.h5ad atac.h5ad -k 5 -o results.csv`
**Explanation:** `-k 5` performs 5-fold cross-validation.