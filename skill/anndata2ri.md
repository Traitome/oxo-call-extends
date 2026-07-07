---
name: anndata2ri
category: formatting
description: RPy2 converter for seamless conversion between AnnData and SingleCellExperiment
tags: [anndata2ri, AnnData, SingleCellExperiment, RPy2, scanpy, seurat, single-cell]
author: oxo-call-community
source_url: "https://github.com/theislab/anndata2ri"
---

## Concepts

- **Tool Overview**: anndata2ri (v2.0) is an RPy2-based converter that enables seamless conversion between Python's AnnData (Scanpy) and R's SingleCellExperiment (Bioconductor) data structures.
- **Core Function**: Facilitates bidirectional conversion between AnnData and SingleCellExperiment objects, enabling cross-language single-cell analysis workflows.
- **Cross-Language Workflow**: Allows users to process data in Python with Scanpy and then transfer to R for Seurat analysis, or vice versa.
- **Activation Modes**: Supports global activation (`anndata2ri.activate()`) or local activation using `localconverter` context manager.
- **Data Preservation**: Preserves key data components including expression matrices, metadata, variable annotations, and reduced dimensions.
- **Installation**: Available via pip (`pip install anndata2ri`) or Bioconda (`conda install -c bioconda anndata2ri`).

## Pitfalls

- **Version Compatibility**: Requires compatible versions of rpy2, anndata, and SingleCellExperiment packages.
- **R Environment**: Requires a properly configured R environment with SingleCellExperiment installed.
- **Data Type Limitations**: Some specialized data types may not convert perfectly between platforms.
- **Memory Considerations**: Large datasets may require significant memory during conversion.
- **Global vs Local Activation**: Global activation affects all rpy2 operations; use local converter for isolated conversions.
- **Dependency Conflicts**: May conflict with other Python-R interoperability tools.

## Examples

### Global activation
**Args:** `import anndata2ri; anndata2ri.activate()`
**Explanation:** Globally activates the converter, enabling automatic conversion between AnnData and SingleCellExperiment.

### Local conversion context
**Args:** `from rpy2.robjects.conversion import localconverter; with localconverter(anndata2ri.converter): ...`
**Explanation:** Creates a local conversion context for isolated conversions without affecting global state.

### Convert AnnData to SingleCellExperiment
**Args:** `import scanpy as sc; adata = sc.read_h5ad('data.h5ad'); r_sce = anndata2ri.py2rpy(adata)`
**Explanation:** Reads AnnData from H5AD file and converts to R SingleCellExperiment object.

### Convert SingleCellExperiment to AnnData
**Args:** `adata = anndata2ri.rpy2py(r_sce)`
**Explanation:** Converts R SingleCellExperiment back to Python AnnData object.

### Scanpy to Seurat workflow
**Args:** `import scanpy as sc; import anndata2ri; from rpy2.robjects.packages import importr; anndata2ri.activate(); seurat = importr('Seurat'); adata = sc.read_h5ad('data.h5ad'); r_sce = anndata2ri.py2rpy(adata); seurat_obj = seurat.CreateSeuratObject(counts=seurat.GetAssayData(r_sce, slot='counts'))`
**Explanation:** Full workflow: read AnnData in Python, convert to SingleCellExperiment, then create Seurat object in R.

### Basic usage in Python script
**Args:** `import anndata2ri; import scanpy as sc; from rpy2.robjects import r; anndata2ri.activate(); adata = sc.AnnData(X=[[1, 2], [3, 4]], obs={'cell': ['A', 'B']}); r.assign('sce', adata); r('sce')`
**Explanation:** Creates AnnData object, converts and assigns to R environment, then prints in R.