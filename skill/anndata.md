---
name: anndata
category: data-structure
description: Python package for handling annotated data matrices in memory and on disk
tags: [anndata, AnnData, single-cell, scanpy, data-structure, h5ad]
author: oxo-call-community
source_url: "https://anndata.readthedocs.io"
---

## Concepts

- **Tool Overview**: anndata (v0.10+) is a Python package for handling annotated data matrices, positioned between pandas and xarray. It provides a canonical data structure for bookkeeping high-dimensional data with annotations.
- **Core Data Structure**: The AnnData object stores:
  - `X`: Main data matrix (n_obs × n_vars), supports sparse and dense formats
  - `obs`: Cell/sample annotations as pandas DataFrame
  - `var`: Feature/gene annotations as pandas DataFrame  
  - `obsm`: Multi-dimensional annotations (e.g., PCA, UMAP embeddings)
  - `varm`: Multi-dimensional variable annotations
  - `obsp`: Pairwise observation matrices (e.g., kNN graph distances)
  - `uns`: Unstructured annotations as dictionary
  - `layers`: Alternative representations of the data matrix
- **Sparse Data Support**: Native support for sparse matrices (CSR, CSC) for memory-efficient storage of scRNA-seq data.
- **On-Disk Storage**: Native HDF5 (.h5ad) and Zarr formats for efficient I/O and out-of-core processing.
- **Scanpy Integration**: Core data structure for Scanpy single-cell analysis toolkit.
- **Installation**: `pip install anndata` or `conda install -c bioconda anndata`

## Pitfalls

- **Version Differences**: API changes between v0.8 and v0.10+; check compatibility when upgrading.
- **Memory Usage**: Large datasets may require HDF5 backing or chunked Zarr storage.
- **Copy vs View**: Slicing AnnData returns views by default; use `.copy()` for independent copies.
- **Sparse Matrix Types**: Operations may differ between sparse formats; convert to consistent type.
- **Layer Management**: Keep track of different data representations (raw counts, normalized, log-transformed).
- **Cross-Language Compatibility**: H5AD format not directly compatible with R; use anndata2ri for conversion.

## Examples

### Create basic AnnData object
**Args:** `import anndata as ad; import numpy as np; adata = ad.AnnData(X=np.array([[1, 2], [3, 4]]), obs={'cell_type': ['A', 'B']}, var={'gene': ['G1', 'G2']})`
**Explanation:** Creates AnnData with 2 cells and 2 genes, including cell and gene annotations.

### Read H5AD file
**Args:** `import anndata as ad; adata = ad.read_h5ad('data.h5ad')`
**Explanation:** Loads AnnData object from HDF5 file. Standard format for sharing single-cell datasets.

### Write H5AD file
**Args:** `adata.write_h5ad('output.h5ad')`
**Explanation:** Saves AnnData object to HDF5 format, preserving all annotations.

### Add PCA embedding
**Args:** `import numpy as np; adata.obsm['X_pca'] = np.random.randn(adata.n_obs, 50)`
**Explanation:** Stores PCA coordinates in obsm for visualization or downstream analysis.

### Add kNN graph
**Args:** `from scipy.sparse import csr_matrix; adata.obsp['connectivities'] = csr_matrix(connectivity_matrix)`
**Explanation:** Stores cell-cell connectivity graph for clustering algorithms.

### Store raw counts
**Args:** `adata.layers['counts'] = adata.X.copy(); adata.X = normalize(adata.X)`
**Explanation:** Preserves raw counts in a layer while working with normalized data in X.

### Slice AnnData
**Args:** `adata_subset = adata[adata.obs['cell_type'] == 'A', :]`
**Explanation:** Subsets AnnData to include only cells of type A. Returns a view by default.

### Convert to dense matrix
**Args:** `dense_matrix = adata.X.toarray()`
**Explanation:** Converts sparse matrix to dense numpy array. Use cautiously for large datasets.