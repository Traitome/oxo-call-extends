---
name: scatac-fragment-tools
category: epigenomics
description: scATAC-Fragment-Tools - Tools for working with scATAC-seq fragment files
tags: ["scatac-fragment-tools", "epigenomics", "ATAC-seq", "single-cell"]
author: oxo-call-community
source_url: "https://aertslab.github.io/scatac_fragment_tools/"
---

## Concepts

- **Tool Overview**: scATAC-Fragment-Tools (v0.1.4) provides utilities for processing and analyzing scATAC-seq fragment data.
- **Core Function**: Manipulates and analyzes fragment files from single-cell ATAC-seq experiments.
- **Algorithm**: Implements efficient operations on fragment data structures.
- **Input/Output**: Accepts fragment files and produces processed data or analysis results.
- **Fragment Analysis**: Focuses on handling sparse fragment data from single cells.
- **Applications**: scATAC-seq data preprocessing, quality control, and downstream analysis.

## Pitfalls

- **ATAC-seq Specific**: Designed specifically for ATAC-seq data.
- **Fragment Quality**: Results depend on input fragment quality.
- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Computational Resources**: May require significant compute resources.
- **File Format**: Requires specific fragment file formats.

## Examples

### Count fragments per cell
**Args:** `scatac-fragment-tools count -i fragments.tsv -o counts.h5ad`
**Explanation:** `-i` input fragment file; `-o` output AnnData with counts.

### Filter fragments
**Args:** `scatac-fragment-tools filter -i fragments.tsv -q 30 -o filtered.tsv`
**Explanation:** `-q 30` filters fragments with quality below 30.

### Merge fragment files
**Args:** `scatac-fragment-tools merge -i frag1.tsv frag2.tsv -o merged.tsv`
**Explanation:** Merges multiple fragment files into one.

### Quality control
**Args:** `scatac-fragment-tools qc -i fragments.tsv -o qc_report.html`
**Explanation:** Generates QC report for fragment data.

### Convert format
**Args:** `scatac-fragment-tools convert -i fragments.tsv -f h5 -o fragments.h5`
**Explanation:** `-f h5` converts to HDF5 format.

### Peak calling
**Args:** `scatac-fragment-tools peaks -i fragments.tsv -o peaks.bed`
**Explanation:** Calls peaks from fragment data.

### Aggregate by cell type
**Args:** `scatac-fragment-tools aggregate -i fragments.tsv -c cell_types.txt -o aggregated.h5ad`
**Explanation:** Aggregates fragments by cell type.