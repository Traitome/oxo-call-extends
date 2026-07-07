---
name: geosketch
category: dimensionality-reduction
description: GeoSketch - Geometry-preserving random sampling for large datasets.
tags: [geosketch, dimensionality-reduction, sampling, single-cell]
author: oxo-call-community
source_url: "https://github.com/brianhie/geosketch"
---

## Concepts
- **Geometry-Preserving Sampling**: Samples data while preserving geometric structure.
- **Dimensionality Reduction**: Reduces dataset size while maintaining structure.
- **Single-Cell Analysis**: Analyzes single-cell RNA-seq data.
- **Data Subsampling**: Subsamples large datasets efficiently.
- **Visualization**: Enables visualization of large datasets.

## Pitfalls
- **Sample Size**: Requires careful selection of sample size.
- **Computational Resources**: Large datasets require resources.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Data Quality**: Depends on input data quality.
- **Result Validation**: Results should be validated.

## Examples
### Sketch dataset
**Args:** `python -c "from geosketch import gs; sketch = gs(X, n=1000)"`
**Explanation:** Creates sketch of dataset with 1000 samples.

### With PCA
**Args:** `python -c "sketch = gs(X, n=1000, pca=True)"`
**Explanation:** Uses PCA for dimensionality reduction before sketching.

### Batch processing
**Args:** `python -c "sketches = [gs(X[i], n=500) for i in range(batches)]"`
**Explanation:** Processes multiple batches.

### Compare methods
**Args:** `python -c "sketch = gs(X, n=1000, method='geosketch')"`
**Explanation:** Specifies sketching method.

### Generate report
**Args:** `python -c "gs.report(X, sketch, 'report.html')"`
**Explanation:** Generates sketching report.