---
name: robust-bias-aware
category: utility
description: Robust bias-aware deconvolution / differential-abundance analysis for high-dimensional biological data; explicitly models and removes technical biases while preserving biological variation.
tags: ["robust-bias-aware", "deconvolution", "bias-correction", "differential-abundance", "statistics", "omics"]
author: oxo-call-community
source_url: "https://github.com/bionetslab/robust_bias_aware_pip_package"
---

## Concepts

- **Tool Overview**: robust-bias-aware (v0.0.1, Bionets Lab) is a Python package for bias-aware deconvolution of high-dimensional biological data (e.g., bulk RNA-Seq, methylation arrays, proteomics). It models technical bias as a low-rank component and biological signal as a sparse component, then separates the two and reports robust estimates of the biological signal.
- **Core Function**: Takes a sample-by-feature count matrix (e.g., genes × samples) and a design matrix encoding known technical covariates (batch, library size, GC content, etc.), and returns a bias-corrected matrix plus per-feature robustness scores. The output is suitable for downstream differential analysis or clustering without the bias confound.
- **Algorithm**: A low-rank-plus-sparse decomposition solved via an ADMM (alternating direction method of multipliers) optimization. The bias matrix is constrained to be low-rank (correlated technical factors), and the biological matrix is constrained to be sparse (only a few features differ between conditions). Robustness is achieved by an L1 penalty on the residual.
- **Input Format**: A TSV/CSV count matrix (rows = features, columns = samples) and a design matrix (rows = samples, columns = technical covariates). Both are pandas DataFrames; the design matrix is optional. Sample IDs in the design matrix must match the count matrix's columns.
- **Output Format**: A pandas DataFrame of the bias-corrected counts, a DataFrame of the per-feature bias contribution, a DataFrame of robustness scores, and a JSON report with the model diagnostics (rank, sparsity, residual norm). All are written to the output directory.
- **Use Case**: Removing batch effects from a multi-site RNA-Seq cohort when the design matrix encodes the site, correcting GC-bias in methylation arrays, normalizing Hi-C contact matrices for restriction-enzyme bias, and deconvolving cell-type proportions from bulk expression while being robust to technical confounders.

## Pitfalls

- **CRITICAL — The design matrix must encode only TECHNICAL covariates**: Including biological covariates (e.g., disease status) in the design matrix absorbs the biological signal into the bias estimate. The result is a bias-corrected matrix that has lost the disease effect. Verify the design matrix is restricted to batch, library prep, sequencer, etc.
- **CRITICAL — The rank of the bias matrix must be set explicitly**: The default rank is 1 (single largest bias direction), but a multi-batch dataset may need rank 2–3. Set via `--rank 3` after exploring with `numpy.linalg.matrix_rank(design_matrix)`.
- **The package requires a Python 3.8+ environment with `cvxpy` and `numpy`**: Older Python versions do not support the `cvxpy` API. Use `conda install -c conda-forge cvxpy` to satisfy the dependency.
- **The bias-correction is linear**: Non-linear biases (e.g., saturation, dropout) are not modeled. For scRNA-Seq, use a dedicated tool (e.g., `scran` or `Seurat::SCTransform`).
- **Memory scales with the number of features**: A 20,000-gene × 1,000-sample matrix requires ~3 GB RAM. For larger matrices, downsample features or use the chunked API.
- **Robustness scores are NOT p-values**: A high robustness score means "the feature's effect is unlikely to be explained by the bias model" — it is a heuristic, not a formal significance test.

## Examples

### Basic bias correction with no design matrix
**Args:** `robust-bias-aware -i counts.tsv -o corrected/`
**Explanation:** `-i` is the count matrix (rows = features, columns = samples), `-o` is the output directory. Without a design matrix, the algorithm estimates the bias direction directly from the data (a single low-rank component).

### With a design matrix
**Args:** `robust-bias-aware -i counts.tsv -d design.tsv -o corrected/`
**Explanation:** `-d` is the design matrix (rows = samples, columns = technical covariates). The bias estimate is projected onto the design matrix's column space, ensuring only the encoded technical factors are removed.

### Increase the bias rank
**Args:** `robust-bias-aware -i counts.tsv -d design.tsv --rank 3 -o corrected/`
**Explanation:** `--rank 3` sets the bias rank to 3, modeling up to three independent technical bias directions. Use when the design matrix has 3+ correlated covariates (e.g., batch + library size + GC content).

### Output a per-feature robustness score
**Args:** `robust-bias-aware -i counts.tsv -d design.tsv --output-robustness -o corrected/`
**Explanation:** `--output-robustness` writes a TSV with a per-feature robustness score (0–1) indicating how much of the feature's variance is explained by the bias model. Use this to filter to features with high biological signal.

### Use the Python API
**Args:** `python -c "from robust_bias_aware import BiasModel; m = BiasModel(rank=2); m.fit(counts_df, design_df); corrected = m.transform(counts_df)"`
**Explanation:** The Python API for embedding robust-bias-aware in a larger pipeline (e.g., a Snakemake rule). `BiasModel` is the main class; `fit` learns the bias model and `transform` applies the correction.

### Apply a learned model to a new dataset
**Args:** `robust-bias-aware --load-model bias_model.pkl -i new_counts.tsv -o corrected_new/`
**Explanation:** `--load-model` loads a previously fit bias model (saved with `pickle`); the correction is applied to the new dataset without re-learning. Useful for batch correction across multiple cohorts.

### Diagnostic plot
**Args:** `robust-bias-aware -i counts.tsv -d design.tsv --plot-diagnostics -o corrected/`
**Explanation:** `--plot-diagnostics` writes a PDF with the per-feature bias contribution, the residual distribution, and the cumulative variance explained. Useful for choosing the rank and checking the model fit.
