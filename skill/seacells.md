---
name: seacells
category: single-cell
description: SEACells - Inference of transcriptional and epigenomic cellular states from single-cell genomics data
tags: ["seacells", "single-cell", "transcriptional-states", "epigenomics"]
author: oxo-call-community
source_url: "https://github.com/dpeerlab/SEACells"
---

## Concepts

- **Tool Overview**: SEACells (v0.3.3) infers transcriptional and epigenomic cellular states from single-cell genomics data.
- **Core Function**: Identifies cellular states by aggregating similar cells into super cells.
- **Algorithm**: Uses graph-based clustering to identify representative cells.
- **Input/Output**: Accepts AnnData objects and produces SEACell representations.
- **Multi-Omics**: Supports integration of multiple omics data types.
- **Applications**: Single-cell analysis, cell state characterization, and data integration.

## Pitfalls

- **Computational Resources**: Requires significant compute resources.
- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Quality**: Results depend on input data quality.
- **Biological Interpretation**: Requires domain knowledge for interpretation.
- **Documentation**: Some features have limited documentation.

## Examples

### Basic analysis
**Args:** `import SEACells; seacells = SEACells.SEACells(adata)`
**Explanation:** Initializes SEACells object.

### Run analysis
**Args:** `seacells.fit()`
**Explanation:** Runs SEACells analysis.

### Get SEACell profiles
**Args:** `seacell_profiles = seacells.seacell_profiles`
**Explanation:** Extracts SEACell profiles.

### Save results
**Args:** `seacells.save('seacells_results.h5ad')`
**Explanation:** Saves results to H5AD file.

### Load results
**Args:** `seacells = SEACells.load('seacells_results.h5ad')`
**Explanation:** Loads previously saved results.

### Plot results
**Args:** `SEACells.plot(seacells, 'umap.png')`
**Explanation:** Generates visualization of results.

### Help command
**Args:** `SEACells --help`
**Explanation:** Shows available commands and options.