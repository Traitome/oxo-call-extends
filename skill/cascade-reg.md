---
name: cascade-reg
category: single-cell
description: Causal discovery of gene regulatory programs from single-cell genomics
tags: [cascade-reg, gene-regulatory-network, single-cell, causality, deep-learning]
author: oxo-call-community
source_url: "https://cascade-reg.readthedocs.io"
---

## Concepts

- **Tool Overview**: CASCADE-REG discovers causal gene regulatory networks from single-cell genomics data using deep learning.
- **Core Function**: Identifies causal relationships between genes and regulatory programs.
- **Algorithm**: Causality-aware deep learning approach for gene regulatory network inference.
- **Input**: Single-cell RNA-seq data and optionally ATAC-seq data.
- **Output**: Causal regulatory network and gene regulatory programs.
- **Application**: Understanding gene regulation in development and disease.
- **Installation**: Install via bioconda: `conda install -c bioconda cascade-reg`

## Pitfalls

- **Data Quality**: Requires high-quality single-cell data with minimal batch effects.
- **Computational Resources**: Deep learning model requires significant GPU memory.
- **Interpretation**: Causal relationships require careful validation.
- **Training Time**: Model training may take hours on large datasets.

## Examples

### Infer regulatory network
**Args:** `cascade-reg -i expression_matrix.h5ad -o regulatory_network.tsv`
**Explanation:** Infers causal gene regulatory network from single-cell RNA-seq data.

### With ATAC-seq integration
**Args:** `cascade-reg -i rna.h5ad -a atac.h5ad -o network.tsv`
**Explanation:** Integrates RNA-seq and ATAC-seq data for improved network inference.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.