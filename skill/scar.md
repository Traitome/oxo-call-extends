---
name: scar
category: single-cell
description: scAR - single-cell Ambient Remover for droplet-based single cell omics
tags: ["scar", "single-cell", "ambient-removal", "deep-learning"]
author: oxo-call-community
source_url: "https://github.com/Novartis/scar"
---

## Concepts

- **Tool Overview**: scAR (v0.7.0) is a deep learning model for ambient signal removal in droplet-based single cell omics.
- **Core Function**: Removes ambient RNA contamination from single-cell sequencing data.
- **Algorithm**: Uses deep learning to distinguish between true cell expression and ambient noise.
- **Input/Output**: Accepts raw count matrices and produces denoised expression data.
- **Ambient RNA**: Addresses the problem of free-floating RNA in droplet-based assays.
- **Applications**: Single-cell RNA-seq data cleaning, improved cell type identification, and downstream analysis.

## Pitfalls

- **Droplet-Based Assays**: Designed specifically for droplet-based sequencing.
- **Training Data**: Requires suitable training data for model training.
- **Computational Resources**: Requires GPU for training and inference.
- **Model Complexity**: May be computationally expensive.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Overfitting Risk**: May overfit to specific datasets.

## Examples

### Basic ambient removal
**Args:** `scar remove -i raw_counts.h5ad -o cleaned.h5ad`
**Explanation:** `-i` input raw data; `-o` cleaned output.

### With trained model
**Args:** `scar remove -i raw_counts.h5ad -m model.pt -o cleaned.h5ad`
**Explanation:** `-m` uses pre-trained model for denoising.

### Train model
**Args:** `scar train -i training_data.h5ad -o model.pt`
**Explanation:** Trains ambient removal model on training data.

### Batch processing
**Args:** `scar batch -i data/*.h5ad -o cleaned/`
**Explanation:** Processes multiple files in batch.

### Verbose logging
**Args:** `scar remove -i raw_counts.h5ad -v -o cleaned.h5ad`
**Explanation:** `-v` enables verbose output for debugging.

### Quality metrics
**Args:** `scar evaluate -i raw_counts.h5ad -o metrics.txt`
**Explanation:** Evaluates ambient removal quality.

### Output report
**Args:** `scar remove -i raw_counts.h5ad --report report.html -o cleaned.h5ad`
**Explanation:** `--report` generates quality report.