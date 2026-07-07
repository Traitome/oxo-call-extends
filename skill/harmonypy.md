---
name: harmonypy
category: bioinformatics
description: HarmonyPy performs data integration and batch effect correction for single-cell sequencing data.
tags: [harmonypy, single-cell, data-integration, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/slowkow/harmonypy"
---

## Concepts

- **Data Integration**: HarmonyPy integrates multiple datasets.

- **Batch Effect Correction**: Corrects batch effects in sequencing data.

- **Single-Cell Analysis**: Optimized for single-cell sequencing data.

- **Dimensionality Reduction**: Performs dimensionality reduction.

- **Clustering**: Supports cell clustering analysis.

- **Visualization**: Aids in data visualization.

## Pitfalls

- **Batch Size**: Ensure balanced batch sizes.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Data Quality**: Results depend on input data quality.

## Examples

### Integrate datasets
**Args:** `python -c "import harmonypy as hm; hm.run_harmony(data, batch_labels)"`
**Explanation:** Integrates single-cell datasets using Harmony.

### With PCA input
**Args:** `python -c "import harmonypy as hm; hm.run_harmony(pca_matrix, batch_labels)"`
**Explanation:** Uses PCA matrix as input for integration.

### Batch processing
**Args:** `for batch in batches: harmonypy.run_harmony(data[batch], batch_labels)`
**Explanation:** Processes multiple batches sequentially.

### Generate report
**Args:** `harmonypy --input data.h5ad --output integrated.h5ad --report`
**Explanation:** Generates integration report.

### Quality filtering
**Args:** `harmonypy --input data.h5ad --min-cells 10 --output filtered.h5ad`
**Explanation:** Filters cells by minimum count.

### Visualization
**Args:** `harmonypy --input data.h5ad --plot --output umap.png`
**Explanation:** Generates UMAP visualization.

### Help command
**Args:** `harmonypy --help`
**Explanation:** Shows available options and usage information.