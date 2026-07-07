---
name: loompy
category: expression
description: loompy - Work with .loom files for single-cell RNA-seq data
tags: [loompy, expression, single-cell, RNA-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/linnarsson-lab/loompy"
---

## Concepts

- **Loom File Format**: Efficient file format for single-cell data
- **Single-cell RNA-seq**: Analysis of single-cell transcriptomics data
- **Data Storage**: Large-scale data storage and retrieval
- **Matrix Operations**: Efficient matrix operations on genomic data
- **Metadata Management**: Metadata handling and annotation
- **Data Integration**: Integration of multiple datasets

## Pitfalls

- **Memory Usage**: Memory-intensive for large datasets
- **File Format**: Strict .loom format requirements
- **Version Compatibility**: API may change between versions
- **Data Integrity**: Requires careful data validation
- **Performance**: May be slow for complex operations
- **Dependency Management**: Requires proper dependency management

## Examples

### Create loom file
**Args:** `import loompy; loompy.create('output.loom', data, row_attrs, col_attrs)`
**Explanation:** Creates a new loom file from data matrix.

### Open loom file
**Args:** `import loompy; with loompy.open('data.loom') as ds: print(ds.shape)`
**Explanation:** Opens and reads from a loom file.

### Access data
**Args:** `ds[:, :100]`
**Explanation:** Accesses first 100 columns of data.

### Add attributes
**Args:** `ds.ra.gene_names = gene_names; ds.ca.cell_types = cell_types`
**Explanation:** Adds row and column attributes.

### Merge files
**Args:** `loompy.merge(['file1.loom', 'file2.loom'], 'merged.loom')`
**Explanation:** Merges multiple loom files.

### Subset data
**Args:** `loompy.create('subset.loom', ds[:, cells], row_attrs=ds.ra, col_attrs=ds.ca[cells])`
**Explanation:** Creates subset of data.