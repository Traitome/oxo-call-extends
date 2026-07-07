---
name: iobrpy
category: bioinformatics
description: Immuno-Oncology Biological Research using Python (IOBRpy)
tags: [iobrpy, immuno-oncology, bioinformatics, tme, immunology, python]
author: oxo-call-community
source_url: "https://github.com/IOBR/IOBRpy"
---

## Concepts

- **Tool Overview**: IOBRpy (v0.1.8) is a Python package for immuno-oncology biological research, focusing on tumor microenvironment (TME) analysis from bulk RNA-seq data.

- **TME Profiling**: Provides comprehensive tools for analyzing the tumor microenvironment, including immune cell infiltration, gene signature scoring, and ligand-receptor interaction analysis.

- **Immune Deconvolution**: Integrates multiple deconvolution algorithms (CIBERSORT, quanTIseq, EPIC, MCPcounter, IPS, ESTIMATE) to estimate immune cell proportions from bulk transcriptomics data.

- **Gene Signature Analysis**: Includes over 200 curated gene signatures related to immunity, metabolism, and cancer pathways. Supports PCA, z-score, and ssGSEA scoring methods.

- **Ligand-Receptor Analysis**: Identifies potential cell-cell communication networks by analyzing ligand-receptor pairs across different cell types.

- **Visualization Tools**: Provides visualization functions for heatmaps, box plots, and TME landscape representations to facilitate result interpretation.

## Pitfalls

- **Input Data Requirements**: Requires TPM-normalized expression data. Raw counts or FPKM values must be converted before analysis.

- **Computational Resources**: Some deconvolution methods (e.g., BayesPrism) require significant computational resources for large datasets.

- **Reference Data Compatibility**: Ensure reference gene signatures and cell type markers match the organism and platform being analyzed.

- **Batch Effect Handling**: Batch effects can significantly affect results. Apply appropriate normalization before running TME analysis.

- **Method Selection**: Different deconvolution methods may produce different results. Consider running multiple methods and comparing outputs.

- **Single-Cell Data**: While primarily designed for bulk RNA-seq, some functions can be adapted for single-cell data with appropriate preprocessing.

## Examples

### All-in-one TME profiling
**Args:** `iobrpy tme_profile -i TPM.csv -o tme_results/ --threads 4`
**Explanation:** Runs the complete TME profiling pipeline including signature scoring, immune deconvolution, and ligand-receptor analysis.

### Calculate gene signature scores
**Args:** `iobrpy calculate_sig_score -i TPM.csv -o sig_scores.csv --signature all --method pca`
**Explanation:** Computes signature scores using PCA-based method for all available gene signatures.

### Run CIBERSORT deconvolution
**Args:** `iobrpy cibersort -i TPM.csv -o cibersort_results.csv --perm 100 --QN True`
**Explanation:** Performs CIBERSORT immune cell deconvolution with quantile normalization and 100 permutations for significance testing.

### Ligand-receptor interaction analysis
**Args:** `iobrpy lr_cal -i TPM.csv -o lr_results.csv --database cellphonedb`
**Explanation:** Identifies ligand-receptor pairs using the CellPhoneDB database to infer cell-cell communication.

### TME clustering analysis
**Args:** `iobrpy tme_cluster -i immune_proportions.csv -o tme_clusters.csv --method kmeans --k 3`
**Explanation:** Performs k-means clustering on immune cell proportions to identify TME subtypes.

### Batch effect removal
**Args:** `iobrpy remove_batch -i raw_counts.csv -o normalized.csv --batch batch_info.txt`
**Explanation:** Removes batch effects from gene expression data using ComBat normalization.