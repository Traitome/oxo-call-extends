---
name: scprep
category: single-cell
description: scprep - Tools for loading and preprocessing biological matrices in Python
tags: ["scprep", "single-cell", "preprocessing", "data-loading"]
author: oxo-call-community
source_url: "https://scprep.readthedocs.io/en/stable/"
---

## Concepts

- **Tool Overview**: scprep (v1.2.3) provides tools for loading and preprocessing biological matrices in Python.
- **Core Function**: Offers utilities for loading, cleaning, and transforming single-cell data.
- **Algorithm**: Implements various preprocessing techniques for biological data.
- **Input/Output**: Accepts various data formats and produces cleaned matrices.
- **Data Integration**: Supports integration with Scanpy and other single-cell tools.
- **Applications**: Single-cell RNA-seq analysis, data preprocessing, and quality control.

## Pitfalls

- **Data Quality**: Results depend on input data quality.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.
- **Performance**: May require optimization for very large datasets.

## Examples

### Load data
**Args:** `import scprep; data = scprep.io.load_csv('data.csv')`
**Explanation:** Loads CSV file into data matrix.

### Filter cells
**Args:** `import scprep; filtered = scprep.filter.filter_cells(data, min_genes=200)`
**Explanation:** Filters cells with minimum 200 genes.

### Normalize data
**Args:** `import scprep; normalized = scprep.normalize.library_size_normalize(data)`
**Explanation:** Applies library size normalization.

### Log transform
**Args:** `import scprep; log_data = scprep.transform.log(data)`
**Explanation:** Applies log transformation.

### Batch correction
**Args:** `import scprep; corrected = scprep.run.ppca(data, batch=batch_labels)`
**Explanation:** Applies PPCA for batch correction.

### Save data
**Args:** `scprep.io.save_csv(data, 'output.csv')`
**Explanation:** Saves data to CSV file.

### Quality control
**Args:** `import scprep; qc_results = scprep.qc.quality_control(data)`
**Explanation:** Performs quality control analysis.