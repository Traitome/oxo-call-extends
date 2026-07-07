---
name: scib
category: single-cell
description: SCIB - Evaluating single-cell data integration methods
tags: ["scib", "single-cell", "integration", "evaluation"]
author: oxo-call-community
source_url: "https://scib.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: SCIB (v1.1.7) provides tools for evaluating single-cell data integration methods.
- **Core Function**: Assesses the quality of single-cell data integration across multiple metrics.
- **Algorithm**: Implements various evaluation metrics for integration quality assessment.
- **Input/Output**: Accepts integrated datasets and produces evaluation metrics.
- **Multi-metric Evaluation**: Uses multiple metrics to assess integration quality.
- **Applications**: Benchmarking integration methods, evaluating batch correction, and method comparison.

## Pitfalls

- **Metric Selection**: Choice of metrics affects evaluation results.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal evaluation.
- **Data Quality**: Results depend on input data quality.
- **Batch Effects**: May not capture all aspects of batch effects.
- **Interpretation**: Requires careful interpretation of multiple metrics.

## Examples

### Basic evaluation
**Args:** `scib evaluate -i integrated.h5ad -o metrics.csv`
**Explanation:** `-i` integrated data; `-o` evaluation metrics.

### Multiple metrics
**Args:** `scib evaluate -i integrated.h5ad -m silhouette,ari,nmi -o metrics.csv`
**Explanation:** `-m` specifies metrics to compute.

### Compare methods
**Args:** `scib compare -i method1.h5ad method2.h5ad -o comparison.csv`
**Explanation:** Compares integration quality across methods.

### Visualize results
**Args:** `scib plot -i metrics.csv -o plot.png`
**Explanation:** Generates visualization of evaluation results.

### Batch effect assessment
**Args:** `scib batch -i integrated.h5ad -b batch -o metrics.csv`
**Explanation:** `-b` specifies batch column for assessment.

### Cell type preservation
**Args:** `scib celltype -i integrated.h5ad -c cell_type -o metrics.csv`
**Explanation:** `-c` specifies cell type column.

### Verbose logging
**Args:** `scib evaluate -i integrated.h5ad -v -o metrics.csv`
**Explanation:** `-v` enables verbose output for debugging.