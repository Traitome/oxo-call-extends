---
name: sincei
category: single-cell
description: sincei - Single-cell epigenomics toolkit
tags: ["sincei", "single-cell", "epigenomics", "scatac"]
author: oxo-call-community
source_url: "https://github.com/bhardwaj-lab/sincei"
---

## Concepts

- **Tool Overview**: sincei (v0.5.2) is a toolkit for single-cell epigenomics data analysis.
- **Core Function**: Performs QC, counting, clustering and visualization.
- **Algorithm**: Uses dimensionality reduction and clustering methods.
- **Input/Output**: Accepts scATAC-seq data and produces analysis results.
- **Single-cell Epigenomics**: Specialized for scATAC-seq analysis.
- **Applications**: Single-cell epigenomics, chromatin accessibility analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Dependency Issues**: Requires Python environment and specific packages.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Run QC
**Args:** `sincei qc -i peaks.h5ad -o qc_report.html`
**Explanation:** `-i` input AnnData; `-o` QC report.

### Count fragments
**Args:** `sincei count -i fragments.tsv -a peaks.bed -o counts.h5ad`
**Explanation:** `-a` peaks file.

### Cluster cells
**Args:** `sincei cluster -i counts.h5ad -o clustered.h5ad`
**Explanation:** Perform clustering analysis.

### Help command
**Args:** `sincei --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sincei --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sincei -v qc -i peaks.h5ad -o qc_report.html`
**Explanation:** `-v` verbose output.

### Plot results
**Args:** `sincei plot -i clustered.h5ad -t umap -o umap.png`
**Explanation:** `-t umap` plot UMAP visualization.
