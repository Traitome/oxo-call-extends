---
name: palantir
category: utility
description: Palantir models continuous cell state and cell fate choices in single-cell data.
tags: [palantir, utility, single-cell, trajectory-analysis]
author: oxo-call-community
source_url: "https://github.com/dpeerlab/palantir"
---

## Concepts

- **Tool Overview**: Palantir analyzes single-cell RNA-seq data for trajectory inference.
- **Core Function**: Models cell differentiation trajectories and fate probabilities.
- **Algorithm**: Uses diffusion maps and entropy-based pseudotime.
- **Input Format**: Accepts AnnData or single-cell expression matrices.
- **Output**: Produces pseudotime values and fate probabilities.
- **Use Case**: Single-cell RNA-seq analysis, cell trajectory inference.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Sensitivity**: Results depend on parameters.
- **Assumptions**: Requires certain data assumptions.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "import palantir; help(palantir)"`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `python -c "import palantir; pr_res = palantir.run_palantir(adata)"`
**Explanation:** Runs Palantir on AnnData object.

### With terminal states
**Args:** `python -c "pr_res = palantir.run_palantir(adata, terminal_states=cells)"`
**Explanation:** Specifies terminal cell states.

### Compute gene expression trends
**Args:** `python -c "trends = palantir.presults.compute_gene_trends(pr_res)"`
**Explanation:** Computes gene expression along trajectory.

### Visualization
**Args:** `python -c "palantir.plot.plot_palantir_results(pr_res)"`
**Explanation:** Visualizes Palantir results.

### Verbose mode
**Args:** `python -c "pr_res = palantir.run_palantir(adata, verbose=True)"`
**Explanation:** Runs with verbose output.

### Number of cores
**Args:** `python -c "pr_res = palantir.run_palantir(adata, n_jobs=8)"`
**Explanation:** Uses 8 cores for parallel processing.