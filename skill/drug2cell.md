---
name: drug2cell
category: annotation
description: "This is a collection of utility functions for gene group activity evaluation in scanpy"
tags: [drug2cell, annotation, single-cell, drug-response, scanpy]
author: oxo-call-community
source_url: "https://github.com/teichlab/drug2cell/"
---

## Concepts

- **Tool Overview**: drug2cell is a collection of utility functions for evaluating gene group activity in single-cell data using scanpy.
- **Core Function**: Assesses drug target gene expression and pathway activity at single-cell resolution.
- **Input/Output**: Input: Single-cell expression data (AnnData). Output: Gene set activity scores, drug response predictions.
- **Algorithm**: Uses gene set enrichment and scoring methods to evaluate pathway activity.
- **Key Features**: Drug target analysis, pathway scoring, cell type-specific responses, integration with scanpy.
- **Installation**: `conda install -c bioconda drug2cell`

## Pitfalls

- **Gene Set Quality**: Results depend on quality of drug target gene sets.
- **Cell Type Bias**: Different cell types may show different baseline expression.
- **Batch Effects**: Technical variation can affect activity scores.
- **Normalization**: Proper data normalization is critical for accurate scoring.
- **Multiple Testing**: Correct for multiple comparisons when testing many drugs.

## Examples

### Basic drug target analysis
**Args:** `--input data.h5ad --drug-targets targets.txt --output results.txt`
**Explanation:** Evaluates drug target gene expression in single-cell data.

### Pathway scoring
**Args:** `--input data.h5ad --pathways pathways.gmt --output scores.txt`
**Explanation:** Scores pathway activity for each cell.

### Cell type specific
**Args:** `--input data.h5ad --drug-targets targets.txt --cell-types clusters.txt --output results.txt`
**Explanation:** Performs drug target analysis for specific cell types.

### Visualization
**Args:** `--input data.h5ad --drug-targets targets.txt --output plot.png --plot`
**Explanation:** Generates visualization of drug target expression.

### Compare conditions
**Args:** `--input data.h5ad --drug-targets targets.txt --conditions condition.txt --output comparison.txt`
**Explanation:** Compares drug target activity between experimental conditions.