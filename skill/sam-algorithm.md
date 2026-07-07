---
name: sam-algorithm
category: single_cell
description: Self-Assembling Manifold algorithm for single-cell RNA-seq analysis
tags: ["sam-algorithm", "single-cell", "RNA-seq", "manifold learning", "visualization"]
author: oxo-call-community
source_url: "https://github.com/atarashansky/self-assembling-manifold"
---

## Concepts

- **Tool Overview**: SAM (Self-Assembling Manifold, v1.0.2) is a dimensionality reduction and visualization algorithm specifically designed for single-cell RNA sequencing data analysis.
- **Core Function**: Maps high-dimensional single-cell transcriptomic data into a low-dimensional manifold for visualization and clustering.
- **Algorithm**: Implements a self-organizing manifold learning approach that preserves local and global structure while enabling efficient visualization of cellular heterogeneity.
- **Input Format**: Single-cell gene expression matrices (AnnData, CSV, Matrix Market), Seurat objects.
- **Output Format**: Low-dimensional embeddings, clustering assignments, visualization coordinates, differential expression results.
- **Use Case**: Single-cell RNA-seq analysis, cell type identification, trajectory inference, developmental biology.

## Pitfalls

- **Computational resources**: Large datasets require significant memory and CPU.
- **Parameter tuning**: May require adjustment for optimal manifold construction.
- **Cell quality**: Poor quality cells may distort the manifold structure.
- **Batch effects**: Batch correction may be required for multi-batch datasets.
- **Memory usage**: Very large datasets may exceed memory limits.
- **Interpretation**: Manifold visualization requires careful biological interpretation.

## Examples

### Basic manifold construction
**Args:** `sam run -i expression_matrix.h5ad -o sam_results`
**Explanation:** `-i` input AnnData object; `-o` output directory.

### With Seurat object
**Args:** `sam run -i seurat_object.rds -o sam_results --format seurat`
**Explanation:** `--format seurat` indicates input is Seurat object.

### Specify resolution
**Args:** `sam run -i expression_matrix.h5ad -o sam_results -r 1.0`
**Explanation:** `-r` clustering resolution parameter.

### Dimensionality reduction
**Args:** `sam run -i expression_matrix.h5ad -o sam_results -d 2`
**Explanation:** `-d` output dimensionality (default: 2).

### Batch correction
**Args:** `sam run -i expression_matrix.h5ad -o sam_results --batch-correct`
**Explanation:** `--batch-correct` enables batch effect correction.

### Trajectory inference
**Args:** `sam run -i expression_matrix.h5ad -o sam_results --trajectory`
**Explanation:** `--trajectory` enables trajectory inference.

### Differential expression
**Args:** `sam de -i sam_results/embedding.h5ad -o de_genes.csv`
**Explanation:** Performs differential expression analysis between clusters.