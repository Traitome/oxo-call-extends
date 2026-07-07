---
name: doubletdetection
category: expression
description: "Method to detect and enable removal of doublets from single-cell RNA-sequencing."
tags: [doubletdetection, expression, single-cell, RNA-seq, doublet-detection]
author: oxo-call-community
source_url: "https://doubletdetection.readthedocs.io"
---

## Concepts

- **Tool Overview**: DoubletDetection is a Python package for detecting doublets (mixed cells) in single-cell RNA sequencing data.
- **Core Function**: Identifies technical artifacts where two cells are captured in the same droplet.
- **Input/Output**: Input: Gene expression matrix (CSV/loom/AnnData). Output: Doublet scores and classifications.
- **Algorithm**: Uses a semi-supervised approach with k-nearest neighbors and probabilistic modeling.
- **Key Features**: High sensitivity, works with various scRNA-seq platforms, batch correction support, visualization tools.
- **Installation**: `conda install -c bioconda doubletdetection`

## Pitfalls

- **Cell Type Mixing**: Doublets from similar cell types are harder to detect than from distinct cell types.
- **Sequencing Depth**: Low-quality cells with few reads can produce false doublet calls.
- **Threshold Selection**: The doublet score cutoff needs careful tuning for each dataset.
- **Batch Effects**: Technical variation between batches can affect doublet detection accuracy.
- **Hyperparameter Sensitivity**: Results can vary with changes to k-nearest neighbor parameters.

## Examples

### Basic doublet detection
**Args:** `--input counts.csv --output doublet_results.csv`
**Explanation:** Detects doublets from a gene expression matrix and outputs results.

### With custom threshold
**Args:** `--input counts.csv --output doublet_results.csv --threshold 0.9`
**Explanation:** Uses a higher confidence threshold (0.9) for calling doublets.

### Batch-aware detection
**Args:** `--input counts.csv --output doublet_results.csv --batch batch_labels.txt`
**Explanation:** Accounts for batch effects when detecting doublets across multiple sequencing runs.

### Generate visualization
**Args:** `--input counts.csv --output doublet_results.csv --plot doublet_plot.png`
**Explanation:** Produces a visualization of doublet scores and cell clustering.

### Multiple samples
**Args:** `--input sample1.csv sample2.csv --output combined_results.csv --merge`
**Explanation:** Processes multiple samples together and merges results into a single output.
