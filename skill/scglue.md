---
name: scglue
category: single-cell
description: scGLUE - Graph-linked unified embedding for unpaired single-cell multi-omics data integration
tags: ["scglue", "single-cell", "multi-omics", "data-integration"]
author: oxo-call-community
source_url: "https://scglue.readthedocs.io"
---

## Concepts

- **Tool Overview**: scGLUE (v0.4.0) provides graph-linked unified embedding for unpaired single-cell multi-omics data integration.
- **Core Function**: Integrates multiple single-cell omics datasets without requiring cell-level pairing.
- **Algorithm**: Uses graph neural networks to learn unified embeddings across modalities.
- **Input/Output**: Accepts multi-omics datasets and produces integrated embeddings.
- **Multi-omics Integration**: Handles scRNA-seq, scATAC-seq, and other modalities.
- **Applications**: Single-cell multi-omics integration, cell type annotation, and cross-modality analysis.

## Pitfalls

- **Computational Resources**: High GPU requirements for training.
- **Data Quality**: Results depend on input data quality.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Training Time**: May require significant training time.
- **Model Complexity**: Complex models may be difficult to interpret.

## Examples

### Basic integration
**Args:** `scglue integrate -i rna.h5ad atac.h5ad -o integrated.h5ad`
**Explanation:** Integrates scRNA-seq and scATAC-seq datasets.

### With graph construction
**Args:** `scglue integrate -i rna.h5ad atac.h5ad --graph -o integrated.h5ad`
**Explanation:** `--graph` enables graph-based integration.

### Train model
**Args:** `scglue train -i rna.h5ad atac.h5ad -o model.pt`
**Explanation:** Trains integration model on multi-omics data.

### Generate embeddings
**Args:** `scglue embed -i data.h5ad -m model.pt -o embeddings.h5ad`
**Explanation:** Generates integrated embeddings using trained model.

### Cell type transfer
**Args:** `scglue transfer -i query.h5ad -m model.pt -o annotations.csv`
**Explanation:** Transfers cell type annotations across modalities.

### Verbose logging
**Args:** `scglue integrate -i rna.h5ad atac.h5ad -v -o integrated.h5ad`
**Explanation:** `-v` enables verbose output for debugging.

### Hyperparameter tuning
**Args:** `scglue train -i rna.h5ad atac.h5ad --lr 0.001 -o model.pt`
**Explanation:** `--lr` sets learning rate for training.