---
name: scanpy-scripts
category: utility
description: Scripts for using scanpy from the command line
tags: ["scanpy-scripts", "utility", "single-cell", "CLI"]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/scanpy-scripts"
---

## Concepts

- **Tool Overview**: scanpy-scripts (v1.9.301) provides command-line scripts for common single-cell analysis tasks using Scanpy.
- **Core Function**: Enables Scanpy functionality through standalone scripts for workflow integration.
- **Algorithm**: Wraps Scanpy's analysis functions for command-line execution.
- **Input/Output**: Accepts various single-cell data formats and produces processed results.
- **Workflow Integration**: Designed for use in pipelines and workflow managers.
- **Applications**: Single-cell data preprocessing, quality control, and analysis automation.

## Pitfalls

- **Scanpy Dependency**: Requires compatible Scanpy version.
- **Function Limitation**: May not cover all Scanpy features.
- **Complex Analysis**: Advanced analysis still requires Python scripting.
- **Error Handling**: Limited error messages compared to Python API.
- **Documentation**: Some scripts may have limited documentation.
- **Version Compatibility**: Scripts may need updates for new Scanpy versions.

## Examples

### Basic preprocessing
**Args:** `scanpy-preprocess -i input.h5ad -o output.h5ad`
**Explanation:** Runs standard preprocessing workflow on single-cell data.

### Quality control
**Args:** `scanpy-qc -i input.h5ad -o qc_report.html`
**Explanation:** Generates quality control report for single-cell data.

### PCA analysis
**Args:** `scanpy-pca -i input.h5ad -n 50 -o output.h5ad`
**Explanation:** `-n 50` performs PCA with 50 components.

### UMAP visualization
**Args:** `scanpy-umap -i input.h5ad -o output.h5ad --plot umap.png`
**Explanation:** Computes UMAP coordinates and generates plot.

### Clustering
**Args:** `scanpy-cluster -i input.h5ad -m leiden -o output.h5ad`
**Explanation:** `-m leiden` performs Leiden clustering.

### Differential expression
**Args:** `scanpy-diffexp -i input.h5ad -g group -o diffexp.csv`
**Explanation:** Performs differential expression analysis.

### Marker genes
**Args:** `scanpy-markers -i input.h5ad -g leiden -o markers.csv`
**Explanation:** Identifies marker genes for each cluster.