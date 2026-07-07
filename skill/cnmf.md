---
name: cnmf
category: expression
description: Consensus NMF for scRNA-Seq data analysis
tags: [cnmf, nmf, single-cell, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/dylkot/cNMF"
---

## Concepts

- **Tool Overview**: cNMF (Consensus Non-negative Matrix Factorization) is a tool for analyzing single-cell RNA sequencing (scRNA-Seq) data using consensus non-negative matrix factorization.
- **Core Function**: Identifies gene expression signatures and cell subpopulations from scRNA-Seq data through consensus matrix factorization.
- **Algorithm**: Uses multiple runs of NMF to generate consensus signatures and robust clustering of cells.
- **Input**: scRNA-Seq expression matrix (genes x cells).
- **Output**: Gene signatures, cell loadings, and consensus clustering results.
- **Application**: Single-cell transcriptomics analysis, cell type identification, and gene expression pattern discovery.
- **Installation**: Install via bioconda: `conda install -c bioconda cnmf`

## Pitfalls

- **Data Normalization**: Requires proper normalization of scRNA-Seq data.
- **Parameter Tuning**: Number of factors (k) needs careful selection.
- **Computational Resources**: May require significant resources for large datasets.
- **Convergence**: Multiple runs needed for consensus, increasing computation time.
- **Interpretation**: Signature interpretation requires biological knowledge.

## Examples

### Run consensus NMF
**Args:** `cnmf -i expression_matrix.txt -o results/`
**Explanation:** Runs consensus NMF on scRNA-Seq expression data.

### With specified k
**Args:** `cnmf -i expression_matrix.txt -k 5 -o results/`
**Explanation:** Runs NMF with 5 factors.

### Multiple iterations
**Args:** `cnmf -i expression_matrix.txt -n 100 -o results/`
**Explanation:** Runs 100 iterations for consensus.

### Display help
**Args:** `cnmf --help`
**Explanation:** Shows all available options and usage information.