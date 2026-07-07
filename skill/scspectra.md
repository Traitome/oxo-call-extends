---
name: scspectra
category: single-cell
description: scSPECTRA - Supervised discovery of interpretable gene programs from single-cell data
tags: ["scspectra", "single-cell", "gene-programs", "interpretability"]
author: oxo-call-community
source_url: "https://github.com/dpeerlab/spectra"
---

## Concepts

- **Tool Overview**: scSPECTRA (v0.2.1) performs supervised discovery of interpretable gene programs from single-cell data.
- **Core Function**: Identifies gene programs that are predictive of cell states or phenotypes.
- **Algorithm**: Uses sparse regression to identify interpretable gene signatures.
- **Input/Output**: Accepts AnnData objects and produces gene program scores.
- **Interpretability**: Designed to produce biologically interpretable results.
- **Applications**: Single-cell RNA-seq analysis, gene signature discovery, and cell state characterization.

## Pitfalls

- **Computational Resources**: May require significant compute resources.
- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Quality**: Results depend on input data quality.
- **Biological Interpretation**: Requires domain knowledge for interpretation.
- **Overfitting**: May overfit to training data.

## Examples

### Basic analysis
**Args:** `import scspectra; results = scspectra.run(adata, labels)`
**Explanation:** Runs scSPECTRA on AnnData object.

### With parameters
**Args:** `results = scspectra.run(adata, labels, n_programs=10)`
**Explanation:** `-n_programs` specifies number of gene programs.

### Plot results
**Args:** `scspectra.plot(results, adata)`
**Explanation:** Visualizes gene program scores.

### Get gene programs
**Args:** `programs = scspectra.get_programs(results)`
**Explanation:** Extracts gene programs from results.

### Save results
**Args:** `scspectra.save(results, 'spectra_results.h5ad')`
**Explanation:** Saves results to H5AD file.

### Load results
**Args:** `results = scspectra.load('spectra_results.h5ad')`
**Explanation:** Loads previously saved results.

### Cross-validation
**Args:** `results = scspectra.cross_validate(adata, labels, k=5)`
**Explanation:** `-k 5` performs 5-fold cross-validation.