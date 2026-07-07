---
name: mofapy2
category: utility
description: Multi-Omics Factor Analysis
tags: [mofapy2, utility, multi-omics]
author: oxo-call-community
source_url: "https://github.com/bioFAM/mofapy2"
---

## Concepts

- **Tool Overview**: MOFA+ v0.7.3 performs Multi-Omics Factor Analysis.
- **Core Function**: Integrates multiple omics data types into latent factors.
- **Multi-Omics Integration**: Combines genomic, transcriptomic, and epigenomic data.
- **Factor Analysis**: Identifies latent factors driving biological variation.
- **Input/Output**: Accepts multi-omics matrices; outputs factor loadings.
- **Systems Biology**: Supports integrative omics analysis.

## Pitfalls

- **Multi-omics Data Required**: Needs multiple data modalities.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal factorization.
- **Data Quality**: Results depend on input data quality.
- **Computational Resources**: Large datasets may require significant resources.
- **Missing Data**: Requires careful handling of missing values.

## Examples

### Run MOFA analysis
**Args:** `python -c "from mofapy2 import run_mofa; run_mofa('config.yaml')"`
**Explanation:** Runs multi-omics factor analysis.

### With custom options
**Args:** `python -c "from mofapy2 import run_mofa; run_mofa('config.yaml', n_factors=10)"`
**Explanation:** Specifies number of factors.

### Plot factors
**Args:** `python -c "from mofapy2 import visualize; visualize.plot_factors('model.hdf5')"`
**Explanation:** Visualizes factor loadings.

### Integrate with scanpy
**Args:** `python -c "import scanpy as sc; sc.external.pp.mofa(adata)"`
**Explanation:** Uses MOFA in scanpy workflow.

### Batch processing
**Args:** `python script.py data/`
**Explanation:** Processes multiple datasets.