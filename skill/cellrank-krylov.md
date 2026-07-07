---
name: cellrank-krylov
category: single-cell
description: CellRank Krylov solver for directed single-cell fate mapping
tags: [cellrank-krylov, cellrank, single-cell, fate-mapping, markov-model]
author: oxo-call-community
source_url: "https://cellrank.org"
---

## Concepts

- **Tool Overview**: cellrank-krylov provides Krylov subspace methods for CellRank's fate mapping.
- **Core Function**: Efficiently computes cellular trajectories using Markov state modeling.
- **Algorithm**: Uses Krylov subspace methods for large-scale eigenvalue problems.
- **Input**: Single-cell RNA-seq data (AnnData format).
- **Output**: Cell fate probabilities and trajectory predictions.
- **Application**: Mapping cellular differentiation paths and lineage tracing.
- **Installation**: Install via bioconda: `conda install -c bioconda cellrank-krylov`

## Pitfalls

- **Data Requirements**: Requires properly preprocessed scRNA-seq data.
- **Computational Resources**: Large datasets may require significant compute.
- **Parameter Tuning**: Transition matrix parameters may need adjustment.
- **Convergence**: Ensure Markov chain converges properly.

## Examples

### Import and initialize
**Args:** `python -c "import cellrank as cr; from cellrank.krylov import *"`
**Explanation:** Imports cellrank and krylov module.

### Compute fate probabilities
**Args:** `cr.krylov.compute_fate_probabilities(adata, n_components=10)`
**Explanation:** Computes fate probabilities using Krylov methods.

### Fit transition matrix
**Args:** `cr.krylov.fit(adata, method='krylov', max_iter=1000)`
**Explanation:** Fits transition matrix using Krylov subspace methods.

### Display help
**Args:** `python -c "from cellrank.krylov import help"`
**Explanation:** Shows available functions and documentation.