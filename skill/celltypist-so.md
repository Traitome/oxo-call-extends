---
name: celltypist-so
category: single-cell
description: Fork of CellTypist without leidenalg dependency for cell type annotation
tags: [celltypist-so, celltypist, single-cell, cell-type-annotation, no-leidenalg]
author: oxo-call-community
source_url: "https://github.com/Mena-SA-Kamel/celltypist-SO"
---

## Concepts

- **Tool Overview**: celltypist-so is a fork of CellTypist without leidenalg package dependency.
- **Core Function**: Provides cell type annotation for scRNA-seq data without requiring leidenalg.
- **Key Difference**: Removes leidenalg dependency to avoid version conflicts and installation issues.
- **Input**: AnnData object with normalized gene expression data.
- **Output**: Cell type predictions with confidence scores.
- **Application**: Single-cell RNA-seq cell type annotation in constrained environments.
- **Installation**: Install via bioconda: `conda install -c bioconda celltypist-so`

## Pitfalls

- **No Over-Clustering**: Without leidenalg, over-clustering features may be limited.
- **Majority Voting**: Majority voting may require alternative clustering method.
- **Model Compatibility**: Ensure models are compatible with this fork version.
- **Version Differences**: May lag behind main CellTypist version updates.

## Examples

### Annotate cells using command line
**Args:** `celltypist annotate --input data.h5ad --model Immune_All_Low.pkl --output annotated.h5ad`
**Explanation:** Annotates cells using pre-trained model without leidenalg dependency.

### List available models
**Args:** `celltypist model --list`
**Explanation:** Lists all available pre-trained models.

### Download specific model
**Args:** `celltypist model --download Immune_All_High.pkl`
**Explanation:** Downloads specific pre-trained model for annotation.

### Display help
**Args:** `celltypist --help`
**Explanation:** Shows all available commands and options.