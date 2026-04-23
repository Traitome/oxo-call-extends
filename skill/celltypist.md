---
name: celltypist
category: annotation
description: Semi-automatic cell type annotation for scRNA-seq data
tags: [celltypist, single-cell, cell-type, annotation, classification, scrna-seq]
author: oxo-call-community
source_url: "https://github.com/Teichlab/celltypist"
---

## Concepts

- **Tool Overview**: CellTypist is an automated cell type annotation tool for scRNA-seq datasets using logistic regression classifiers optimized by stochastic gradient descent.
- **Core Function**: Assigns cell type labels to single-cell data by comparing expression profiles against pre-trained models from the CellTypist model repository.
- **Input/Output**: Input: AnnData object with normalized expression. Output: Cell type labels with confidence scores, can be integrated into AnnData.
- **Model Repository**: Provides 48+ pre-trained models covering immune cells, brain, pancreas, and other tissues. Models are downloaded automatically.
- **Two Modes**: Command-line interface (`celltypist`) and Python API. Python API offers more flexibility for customization.
- **Majority Voting**: Uses a majority voting approach across similar cells to refine annotations and reduce noise.

## Pitfalls

- **Model Selection**: Choose a model that matches your tissue/sample type. Using an inappropriate model produces incorrect annotations.
- **Normalization**: Input data should be log-normalized (log1p). Raw counts need preprocessing before annotation.
- **Over-clustering**: Default `over_clustering` may be too aggressive. Adjust `use_over_clustering` parameter or provide custom clustering.
- **Unknown Labels**: Cells with low prediction scores are labeled "Unknown" by default. Adjust `majority_voting` threshold if needed.
- **Species Compatibility**: Most models are trained on human data. Mouse data may require cross-species ortholog mapping first.

## Examples

### Annotate cells using command line
**Args:** `celltypist annotate --input data.h5ad --model Immune_All_Low.pkl --output annotated.h5ad`
**Explanation:** Annotates cells using the Immune_All_Low model (low-resolution immune cell types), outputs annotated AnnData.

### List available models
**Args:** `celltypist model --list`
**Explanation:** Lists all available pre-trained models in the CellTypist repository.

### Download a specific model
**Args:** `celltypist model --download Immune_All_High.pkl`
**Explanation:** Downloads the high-resolution immune cell model for offline use.

### Annotate with majority voting
**Args:** `celltypist annotate --input data.h5ad --model Immune_All_Low.pkl --majority-voting --output annotated.h5ad`
**Explanation:** Applies majority voting to refine annotations by considering neighboring cells, reducing noise in predictions.

### Python API: Basic annotation
**Args:** `predictions = celltypist.annotate(adata, model="Immune_All_Low.pkl", majority_voting=True)`
**Explanation:** Uses Python API for annotation with majority voting, returns predictions object with labels and scores.

### Python API: Custom model training
**Args:** `celltypist.train(custom_adata, labels="cell_type", output_file="custom_model.pkl")`
**Explanation:** Trains a custom CellTypist model from your own annotated dataset for domain-specific annotation.

### Annotate with specific over-clustering
**Args:** `celltypist annotate --input data.h5ad --model Immune_All_Low.pkl --over-clustering leiden --output annotated.h5ad`
**Explanation:** Uses leiden clustering for majority voting instead of default over-clustering approach.
