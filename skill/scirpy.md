---
name: scirpy
category: single-cell
description: scirpy - A Scanpy extension for analyzing single-cell T-cell and B-cell receptor (TCR/BCR) sequencing data
tags: ["scirpy", "single-cell", "TCR", "BCR", "immune-repertoire"]
author: oxo-call-community
source_url: "https://scirpy.scverse.org/en/latest"
---

## Concepts

- **Tool Overview**: scirpy (v0.23.0) is a Scanpy extension for analyzing single-cell T-cell and B-cell receptor (TCR/BCR) sequencing data.
- **Core Function**: Provides tools for analyzing immune receptor repertoires from single-cell data.
- **Algorithm**: Implements various algorithms for TCR/BCR analysis and clonotype identification.
- **Input/Output**: Accepts AnnData objects and produces immune repertoire analysis results.
- **Integration**: Seamlessly integrates with Scanpy for comprehensive single-cell analysis.
- **Applications**: Immune repertoire analysis, clonotype tracking, and TCR/BCR sequencing data analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Data Quality**: Results depend on input data quality and sequencing depth.
- **Clonotype Definition**: Clonotype definition affects analysis results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Computational Resources**: May require significant compute resources.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Basic analysis
**Args:** `import scirpy; adata = scirpy.read_10x_vdj('vdj_data/')`
**Explanation:** Reads 10x Genomics V(D)J data into AnnData object.

### Clonotype analysis
**Args:** `import scirpy; scirpy.pp.ir_dist(adata)`
**Explanation:** Computes distance between immune receptor sequences.

### Clonotype network
**Args:** `import scirpy; scirpy.pl.clonotype_network(adata, color='cell_type')`
**Explanation:** Visualizes clonotype network.

### Repertoire diversity
**Args:** `import scirpy; diversity = scirpy.tl.repertoire_diversity(adata)`
**Explanation:** Calculates repertoire diversity metrics.

### Clonotype expansion
**Args:** `import scirpy; scirpy.tl.clonotype_expansion(adata)`
**Explanation:** Identifies expanded clonotypes.

### Export results
**Args:** `adata.write('scirpy_results.h5ad')`
**Explanation:** Saves analysis results to H5AD file.

### Merge with gene expression
**Args:** `import scirpy; adata_merged = scirpy.pp.merge_with_rna(adata_vdj, adata_rna)`
**Explanation:** Merges V(D)J data with gene expression data.