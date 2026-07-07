---
name: scvelo
category: single-cell
description: scVelo - Single-cell RNA velocity generalized to transient cell states
tags: ["scvelo", "single-cell", "RNA-velocity", "trajectory"]
author: oxo-call-community
source_url: "https://github.com/theislab/scvelo"
---

## Concepts

- **Tool Overview**: scVelo (v0.2.5) performs single-cell RNA velocity analysis generalized to transient cell states.
- **Core Function**: Analyzes RNA velocity to infer cell trajectories and differentiation dynamics.
- **Algorithm**: Uses splicing kinetics to estimate RNA velocity.
- **Input/Output**: Accepts AnnData objects and produces velocity estimates.
- **Transient States**: Handles both steady-state and transient cell states.
- **Applications**: Single-cell trajectory analysis, differentiation studies, and developmental biology.

## Pitfalls

- **Computational Resources**: Requires significant compute resources.
- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Quality**: Results depend on sequencing depth and quality.
- **GPU Availability**: Performance benefits from GPU acceleration.
- **Biological Interpretation**: Requires domain knowledge for interpretation.

## Examples

### Basic velocity analysis
**Args:** `import scvelo as scv; adata = scv.read('data.h5ad')`
**Explanation:** Reads AnnData object.

### Compute velocity
**Args:** `scv.pp.filter_and_normalize(adata); scv.pp.moments(adata); scv.tl.velocity(adata)`
**Explanation:** Computes RNA velocity.

### Visualize velocity
**Args:** `scv.pl.velocity_embedding(adata, basis='umap')`
**Explanation:** Plots velocity vectors on UMAP.

### Save results
**Args:** `adata.write('velocity_results.h5ad')`
**Explanation:** Saves results to H5AD file.

### Load results
**Args:** `adata = scv.read('velocity_results.h5ad')`
**Explanation:** Loads previously saved results.

### Differential velocity
**Args:** `scv.tl.rank_velocity_genes(adata, groupby='cell_type')`
**Explanation:** Identifies velocity-driving genes.

### Cluster cells
**Args:** `scv.tl.louvain(adata)`
**Explanation:** Performs Louvain clustering.