---
name: simba
category: single-cell
description: SIMBA - Single-cell embedding along with features
tags: ["simba", "single-cell", "embedding", "multi-omics"]
author: oxo-call-community
source_url: "https://github.com/huidongchen/simba"
---

## Concepts

- **Tool Overview**: SIMBA (v1.2) performs single-cell embedding with feature integration.
- **Core Function**: Integrates multi-omics data for single-cell analysis.
- **Algorithm**: Uses graph-based embedding approach for data integration.
- **Input/Output**: Accepts gene expression and chromatin accessibility data.
- **Multi-omics Integration**: Specialized for integrating different data modalities.
- **Applications**: Single-cell multi-omics analysis, cell type identification.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Run SIMBA analysis
**Args:** `simba -i data.h5ad -o results/`
**Explanation:** `-i` input AnnData object; `-o` output directory.

### With multiple modalities
**Args:** `simba -i rna.h5ad -c atac.h5ad -o results/`
**Explanation:** `-i` RNA data; `-c` ATAC-seq data.

### With preprocessing
**Args:** `simba -i data.h5ad --preprocess -o results/`
**Explanation:** `--preprocess` enable automatic preprocessing.

### Help command
**Args:** `simba --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simba --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simba -v -i data.h5ad -o results/`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `simba -t 8 -i data.h5ad -o results/`
**Explanation:** `-t 8` uses 8 threads.
