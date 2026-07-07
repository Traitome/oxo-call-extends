---
name: scanpy-cli
category: utility
description: CLI for Scanpy - command-line interface for single-cell analysis
tags: ["scanpy-cli", "utility", "single-cell", "CLI"]
author: oxo-call-community
source_url: "https://github.com/nictru/scanpy-cli"
---

## Concepts

- **Tool Overview**: scanpy-cli (v0.2.0) is a command-line interface for Scanpy, enabling common single-cell analysis tasks from the command line.
- **Core Function**: Provides CLI access to Scanpy's core functionality without Python scripting.
- **Algorithm**: Wraps Scanpy's Python API for command-line usage.
- **Input/Output**: Accepts AnnData files and produces processed single-cell data.
- **Workflow Integration**: Enables integration with shell scripts and workflow managers.
- **Applications**: Single-cell data preprocessing, clustering, and visualization from CLI.

## Pitfalls

- **Scanpy Dependency**: Requires Scanpy installation.
- **Function Limitation**: May not support all Scanpy features.
- **Complex Pipelines**: Complex analysis may still require Python scripting.
- **Version Compatibility**: Depends on specific Scanpy version.
- **Error Handling**: Limited error messages compared to Python API.
- **Documentation**: Limited documentation for CLI-specific features.

## Examples

### Basic preprocessing
**Args:** `scanpy preprocess -i data.h5ad -o processed.h5ad`
**Explanation:** Runs basic preprocessing on single-cell data.

### PCA analysis
**Args:** `scanpy pca -i data.h5ad -n 50 -o pca.h5ad`
**Explanation:** `-n 50` performs PCA with 50 components.

### Clustering
**Args:** `scanpy cluster -i data.h5ad -m leiden -o clustered.h5ad`
**Explanation:** `-m leiden` uses Leiden clustering algorithm.

### Visualization
**Args:** `scanpy plot -i data.h5ad -t umap -o umap.png`
**Explanation:** `-t umap` generates UMAP visualization.

### Differential expression
**Args:** `scanpy diffexp -i data.h5ad -g group -o diffexp.csv`
**Explanation:** Performs differential expression analysis.

### Filter cells
**Args:** `scanpy filter -i data.h5ad -min_genes 200 -max_genes 2500 -o filtered.h5ad`
**Explanation:** Filters cells based on gene counts.

### Normalize data
**Args:** `scanpy normalize -i data.h5ad -t log1p -o normalized.h5ad`
**Explanation:** `-t log1p` applies log normalization.