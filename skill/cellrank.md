---
name: cellrank
category: expression
description: Directed single-cell fate mapping using Markov state modeling
tags: [cellrank, single-cell, fate-mapping, trajectory, rna-velocity, scrna-seq]
author: oxo-call-community
source_url: "https://github.com/dpeerlab/cellrank"
---

## Concepts

- **Tool Overview**: CellRank is a scalable framework for computing directed cell-state trajectories and uncovering cellular dynamics from single-cell data using Markov state modeling.
- **Core Function**: Combines transcriptomic similarity with directionality information (e.g., RNA velocity) to predict cell fate probabilities and identify driver genes.
- **Two Main Modules**: Kernels compute cell-cell transition probabilities; Estimators generate hypotheses (fate probabilities, driver genes, terminal states) from these probabilities.
- **Input**: AnnData object with RNA velocity or other directionality information. Can work with scVelo, Palantir, or other velocity tools.
- **Multiview Support (v2)**: CellRank 2 integrates multiple data modalities (transcriptomics, epigenomics, proteomics) for unified fate mapping.
- **Python API**: Primarily used as a Python library, not a command-line tool. Typical workflow: import cellrank, create kernel, compute transition matrix, fit estimator.

## Pitfalls

- **Requires Directionality**: CellRank needs directionality information (RNA velocity, pseudotime, etc.). Without it, use `PseudotimeKernel` or `RealTimeKernel`.
- **Kernel Selection**: Choose the appropriate kernel for your data: `VelocityKernel` for RNA velocity, `PseudotimeKernel` for pseudotime, `CytoTRACEKernel` for differentiation potential.
- **Memory Usage**: Large datasets (>100k cells) may require significant memory. Consider downsampling or using sparse matrices.
- **Convergence Issues**: GPCCA estimator may not converge. Adjust `n_cells` parameter or increase `n_states` for initial macrostate calculation.
- **Version Differences**: CellRank 1.x and 2.x have different APIs. CellRank 2 uses `cellrank.kernels` and `cellrank.estimators` modules.

## Examples

### Basic workflow with velocity kernel
**Args:** `VelocityKernel(adata).compute_transition_matrix().GPCCA.fit().predict()`
**Explanation:** Creates a velocity kernel from AnnData with RNA velocity, computes transition matrix, fits GPCCA estimator, and predicts terminal states.

### Use pseudotime kernel without velocity
**Args:** `PseudotimeKernel(adata, time_key="dpt_pseudotime").compute_transition_matrix()`
**Explanation:** Uses diffusion pseudotime as directionality when RNA velocity is not available.

### Compute fate probabilities
**Args:** `estimator = GPCCA(vk); estimator.fit(n_states=[3, 6]); estimator.predict(); estimator.fate_probabilities`
**Explanation:** Fits GPCCA with a range of macrostates, predicts terminal states, and retrieves fate probabilities for each cell.

### Identify driver genes
**Args:** `estimator.compute_lineage_drivers(lineages=["Alpha", "Beta"])`
**Explanation:** Identifies genes that drive differentiation toward Alpha and Beta cell fates.

### Combine multiple kernels
**Args:** `k = 0.8 * VelocityKernel(adata) + 0.2 * ConnectivityKernel(adata); k.compute_transition_matrix()`
**Explanation:** Combines velocity and connectivity kernels with custom weights for more robust transition matrix.

### Use CytoTRACE kernel
**Args:** `CytoTRACEKernel(adata).compute_transition_matrix()`
**Explanation:** Uses CytoTRACE differentiation potential as directionality, no velocity required.
