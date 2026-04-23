---
name: brooklyn_plot
category: expression
description: Gene co-expression and transcriptional bursting pattern recognition in single-cell RNA-seq
tags: [brooklyn, single-cell, rna-seq, co-expression, bursting]
author: oxo-call-community
source_url: "https://github.com/arunhpatil/brooklyn/"
---

## Concepts

- **Tool Overview**: Brooklyn Plot analyzes gene co-expression and transcriptional bursting in single-cell RNA-seq.
- **Core Function**: Identifies co-expression patterns and bursting dynamics from scRNA-seq data.
- **Input**: Single-cell expression matrix.
- **Output**: Co-expression networks and bursting parameter estimates.
- **Application**: Understanding transcriptional regulation at single-cell resolution.
- **Installation**: Install via bioconda: `conda install -c bioconda brooklyn_plot`

## Pitfalls

- **Data Normalization**: Input data should be properly normalized.
- **Sparsity**: scRNA-seq data is sparse; results depend on dropout handling.
- **Cell Type**: Different cell types may have different bursting dynamics.

## Examples

### Analyze co-expression
**Args:** `brooklyn_plot -i expression_matrix.h5 -o coexpression_results/`
**Explanation:** Analyzes gene co-expression patterns from single-cell data.

### Detect bursting patterns
**Args:** `brooklyn_plot -i expression.h5 --bursting -o bursting_results/`
**Explanation:** Identifies transcriptional bursting patterns in gene expression.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
