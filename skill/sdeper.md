---
name: sdeper
category: spatial
description: sdeper - Spatial Deconvolution method with Platform Effect Removal
tags: ["sdeper", "spatial", "deconvolution", "platform-effect"]
author: oxo-call-community
source_url: "https://sdeper.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: sdeper (v2.0.0) performs spatial deconvolution with platform effect removal.
- **Core Function**: Deconvolves spatial transcriptomics data to identify cell type proportions.
- **Algorithm**: Uses statistical methods to remove platform effects and deconvolve mixed signals.
- **Input/Output**: Accepts spatial expression data and produces cell type proportions.
- **Platform Effect Removal**: Specifically designed to handle platform-specific biases.
- **Applications**: Spatial transcriptomics analysis, cell type deconvolution, and spatial mapping.

## Pitfalls

- **Computational Resources**: May require significant compute resources.
- **Memory Usage**: High memory requirements for large datasets.
- **Reference Data**: Requires high-quality reference single-cell data.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Biological Interpretation**: Requires domain knowledge for interpretation.
- **Documentation**: Some features have limited documentation.

## Examples

### Basic deconvolution
**Args:** `sdeper deconvolve -i spatial.h5ad -r reference.h5ad -o proportions.csv`
**Explanation:** `-i` spatial data; `-r` reference; `-o` output proportions.

### With platform effect removal
**Args:** `sdeper deconvolve -i spatial.h5ad -r reference.h5ad --remove-platform -o proportions.csv`
**Explanation:** `--remove-platform` enables platform effect removal.

### Verbose logging
**Args:** `sdeper deconvolve -i spatial.h5ad -r reference.h5ad -v -o proportions.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `sdeper deconvolve -i spatial.h5ad -r reference.h5ad -t 8 -o proportions.csv`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Quality check
**Args:** `sdeper quality -i spatial.h5ad -o qc_report.pdf`
**Explanation:** Generates quality control report.

### Batch correction
**Args:** `sdeper correct -i spatial.h5ad -b batches.txt -o corrected.h5ad`
**Explanation:** Performs batch correction.

### Help command
**Args:** `sdeper --help`
**Explanation:** Shows available commands and options.