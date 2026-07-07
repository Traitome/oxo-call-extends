---
name: multivelo
category: utility
description: MultiVelo is a single-cell multi-omic extension of RNA velocity that integrates chromatin accessibility with transcriptomic data.
tags: [multivelo, rna-velocity, single-cell, multi-omic, chromatin, atac-seq, scRNA-seq, gene-regulation]
author: oxo-call-community
source_url: "https://github.com/welch-lab/MultiVelo"
---

## Concepts

- **Tool Overview**: MultiVelo v0.1.3 is a mechanistic model that extends RNA velocity to incorporate chromatin accessibility data. It uses a probabilistic latent variable framework to estimate switch time and rate parameters of gene regulation.
- **Core Function**: Integrates scRNA-seq (spliced/unspliced counts) with scATAC-seq or snATAC-seq data to model the temporal relationship between epigenetic and transcriptomic changes during differentiation.
- **Algorithm**: Uses ordinary differential equations (ODE) to model transcription, splicing, and chromatin state transitions. Estimates parameters including RNA synthesis rate (α), splicing rate (β), degradation rate (γ), and chromatin opening rate (k_c).
- **Input**: Expects AnnData objects with RNA layers (spliced/unspliced) and ATAC data (peaks/ accessibility). Works with 10X Multiome, SHARE-seq, and similar paired or independent modalities.
- **Output**: Returns velocity estimates, latent time, velocity genes, and phase portrait plots. Quantifies concordance/discordance between chromatin and transcription states.
- **Installation**: Install via pip (`pip install multivelo`) or Bioconda (`conda install -c bioconda multivelo`). Requires Python >= 3.7, scanpy, scvelo, and scipy.

## Pitfalls

- **Data Quality Requirements**: Multiome or paired ATAC+RNA data is required for the full model. RNA-only velocity is supported but loses the chromatin integration advantage.
- **Cell Filtering**: Low-quality cells with poor RNA counts or ATAC signal will degrade model fitting. Pre-filter cells using standard scanpy thresholds (min_genes=200, min_cells=3).
- **Peak Annotation**: ATAC peaks must be annotated to genes for model fitting. Use GREAT or similar tools for peak-gene assignment. Incorrect annotation leads to meaningless results.
- **Shared Barcodes**: RNA and ATAC data must share cell barcodes. Ensure barcode compatibility between modalities before analysis. Barcode mismatch is a common failure mode.
- **Computational Cost**: Model fitting across all genes is computationally intensive. Start with highly variable genes and subset for initial exploration before scaling up.
- **Parameter Estimation**: The ODE solver may fail to converge for genes with poor signal. Check fit_r2 values and exclude genes with low R-squared from interpretation.

## Examples

### Basic velocity analysis with multiome data
**Args:** `multivelo.analyze(adata_rna, adata_atac)`
**Explanation:** Runs the full multi-omic dynamical model on RNA and ATAC data. Requires both AnnData objects with proper layers (Mu, Ms for RNA; Mc for ATAC).

### Recover dynamics with chromatin integration
**Args:** `mv.recover_dynamics_chrom(adata_rna, adata_atac, gene_list)`
**Explanation:** Fits the mechanistic model with chromatin accessibility for specified genes. Returns parameter estimates (alpha, beta, gamma, k_c) and timing information.

### Compute velocity and latent time
**Args:** `mv.velocity_graph(adata_result); mv.latent_time(adata_result)`
**Explanation:** Computes velocity vectors and estimates global latent time after model fitting. Latent time provides a unified trajectory ordering.

### Set velocity genes with custom thresholds
**Args:** `mv.set_velocity_genes(adata, likelihood_lower=0.05, alpha_upper=10)`
**Explanation:** Resets velocity gene selection criteria. Filters genes by likelihood and parameter bounds to focus on well-fitted genes for downstream analysis.

### Visualize chromatin-RNA dynamics
**Args:** `mv.velocity_chrom(adata_rna, adata_atac, gene_list=['GENE1','GENE2'], save_plot=True, plot_dir='plots/')`
**Explanation:** Generates phase portrait plots showing relationship between chromatin accessibility and RNA expression over pseudotime. Useful for mechanistic interpretation.

### Run in stochastic mode for large datasets
**Args:** `mv.recover_dynamics_chrom(adata_rna, adata_atac, mode='stochastic', parallel=True, n_jobs=8)`
**Explanation:** Uses stochastic moment matching instead of deterministic integration for faster computation on large datasets. Enables parallel processing with 8 cores.
