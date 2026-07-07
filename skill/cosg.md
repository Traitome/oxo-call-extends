---
name: cosg
category: metagenomics
description: Accurate and fast cell marker gene identification
tags: [cosg, cell-marker, single-cell, gene-identification, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/genecell/COSG"
---

## Concepts

- **Tool Overview**: COSG (Cell marker gene identification using graph-based method) is an accurate and fast tool for identifying cell marker genes from single-cell RNA sequencing data.
- **Core Function**: Identifies marker genes that are specifically expressed in particular cell types or clusters.
- **Algorithm**: Uses graph-based methods and statistical analysis to detect cell-type-specific marker genes.
- **Input**: Single-cell RNA-seq expression matrix, cell type annotations or clustering results.
- **Output**: Ranked list of marker genes for each cell type/cluster, statistical significance scores.
- **Application**: Single-cell RNA-seq analysis, cell type identification, marker gene discovery.
- **Installation**: Install via bioconda: `conda install -c bioconda cosg`

## Pitfalls

- **Data Quality**: Requires high-quality single-cell RNA-seq data with minimal dropout.
- **Cell Type Annotation**: Accurate cell type labels improve marker gene identification.
- **Expression Thresholds**: Choosing appropriate expression thresholds affects results.
- **Batch Effects**: Batch effects may confound marker gene identification.
- **Computational Resources**: Large datasets may require significant memory.

## Examples

### Identify marker genes
**Args:** `cosg -i expression_matrix.csv -c cell_types.txt -o marker_genes.txt`
**Explanation:** Identifies marker genes for each cell type.

### With clustering results
**Args:** `cosg -i expression_matrix.csv -k clusters.txt -o marker_genes.txt`
**Explanation:** Uses clustering results instead of cell type annotations.

### Filter by specificity
**Args:** `cosg -i expression_matrix.csv -c cell_types.txt -s 0.8 -o marker_genes.txt`
**Explanation:** Filters marker genes by specificity score (0.8 threshold).

### Generate visualization
**Args:** `cosg -i expression_matrix.csv -c cell_types.txt --plot -o marker_plot.png`
**Explanation:** Generates visualization of marker gene expression.

### Display help
**Args:** `cosg --help`
**Explanation:** Shows all available options and usage information.