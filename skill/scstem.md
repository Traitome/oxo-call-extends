---
name: scstem
category: single-cell
description: scSTEM - Mapping single-cell and spatial transcriptomics data with transfer learning
tags: ["scstem", "single-cell", "spatial-transcriptomics", "transfer-learning"]
author: oxo-call-community
source_url: "https://github.com/WhirlFirst/STEM"
---

## Concepts

- **Tool Overview**: scSTEM (v0.0.2) maps single-cell and spatial transcriptomics data using transfer learning.
- **Core Function**: Aligns spatial transcriptomics data to single-cell reference datasets.
- **Algorithm**: Uses transfer learning for improved mapping accuracy.
- **Input/Output**: Accepts AnnData objects and produces mapped results.
- **Transfer Learning**: Leverages pre-trained models for better performance.
- **Applications**: Spatial transcriptomics analysis, data integration, and cell type mapping.

## Pitfalls

- **Computational Resources**: Requires significant compute resources, especially GPU.
- **Memory Usage**: High memory requirements for large datasets.
- **Training Time**: May require long training times.
- **Reference Quality**: Results depend on reference dataset quality.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **GPU Availability**: Performance benefits from GPU acceleration.

## Examples

### Basic mapping
**Args:** `scstem map -i spatial.h5ad -r reference.h5ad -o mapped.h5ad`
**Explanation:** `-i` spatial data; `-r` reference; `-o` mapped output.

### Train model
**Args:** `scstem train -i reference.h5ad -o model.pt`
**Explanation:** Trains mapping model on reference data.

### Load model
**Args:** `scstem map -i spatial.h5ad -m model.pt -o mapped.h5ad`
**Explanation:** Uses pre-trained model for mapping.

### Verbose logging
**Args:** `scstem map -i spatial.h5ad -r reference.h5ad -v -o mapped.h5ad`
**Explanation:** `-v` enables verbose output for debugging.

### Cross-validation
**Args:** `scstem cv -i data.h5ad -k 5 -o results.csv`
**Explanation:** `-k 5` performs 5-fold cross-validation.

### Hyperparameter tuning
**Args:** `scstem tune -i data.h5ad -p params.json -o best_model.pt`
**Explanation:** `-p` specifies hyperparameter file.

### Visualization
**Args:** `scstem plot -i mapped.h5ad -o umap.png`
**Explanation:** Generates visualization of mapped data.