---
name: mnnpy
category: programming
description: Mutual nearest neighbors correction in python.
tags: [mnnpy, programming, bioinformatics]
author: oxo-call-community
source_url: "http://github.com/chriscainx/mnnpy"
---

## Concepts

- **Tool Overview**: mnnpy v0.1.9.5 performs mutual nearest neighbors correction.
- **Core Function**: Implements MNN correction for batch effect removal.
- **Batch Effect Removal**: Corrects technical variation between batches.
- **Single-cell Analysis**: Optimized for single-cell RNA-seq data.
- **Input/Output**: Accepts gene expression matrices; outputs corrected data.
- **Integration**: Supports integration with scanpy and other scRNA-seq tools.

## Pitfalls

- **Single-cell Specific**: Designed for single-cell sequencing data.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal correction.
- **Data Quality**: Results depend on input data quality.
- **Batch Identification**: Requires batch labels for correction.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Correct batch effects
**Args:** `python -c "import mnnpy; corrected = mnnpy.mnn_correct(data1, data2)"`
**Explanation:** Corrects batch effects between two datasets.

### With multiple batches
**Args:** `python -c "import mnnpy; corrected = mnnpy.mnn_correct(*datasets)"`
**Explanation:** Corrects multiple batches simultaneously.

### Custom parameters
**Args:** `python -c "import mnnpy; corrected = mnnpy.mnn_correct(data1, data2, k=20)"`
**Explanation:** Uses custom number of nearest neighbors.

### Integration with scanpy
**Args:** `python -c "import scanpy as sc; import mnnpy; sc.pp.mnn_correct(adata)"`
**Explanation:** Uses MNN correction in scanpy workflow.

### Batch processing
**Args:** `python script.py data/`
**Explanation:** Processes multiple datasets.