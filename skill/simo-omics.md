---
name: simo-omics
category: single-cell
description: SIMO - Spatial integration of multi-omics single-cell datasets
tags: ["simo-omics", "single-cell", "multi-omics", "integration"]
author: oxo-call-community
source_url: "https://github.com/ZJUFanLab/SIMO"
---

## Concepts

- **Tool Overview**: SIMO (v1.0.0) integrates multi-omics single-cell datasets through probabilistic alignment.
- **Core Function**: Aligns and integrates spatial multi-omics data.
- **Algorithm**: Uses probabilistic alignment for data integration.
- **Input/Output**: Accepts multiple omics datasets and produces integrated results.
- **Spatial Integration**: Specialized for spatial transcriptomics and multi-omics.
- **Applications**: Spatial biology, single-cell multi-omics analysis.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on data quality.
- **Version Compatibility**: Early development stage, API may change.
- **Documentation**: Limited documentation available.

## Examples

### Integrate datasets
**Args:** `simo-omics -i rna.h5ad -s spatial.h5ad -o integrated.h5ad`
**Explanation:** `-i` RNA data; `-s` spatial data; `-o` output.

### With multiple modalities
**Args:** `simo-omics -i rna.h5ad -a atac.h5ad -s spatial.h5ad -o integrated.h5ad`
**Explanation:** `-a` ATAC-seq data.

### With alignment
**Args:** `simo-omics -i data1.h5ad -j data2.h5ad -a -o aligned.h5ad`
**Explanation:** `-a` perform alignment.

### Help command
**Args:** `simo-omics --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simo-omics --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simo-omics -v -i rna.h5ad -s spatial.h5ad -o integrated.h5ad`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `simo-omics -t 8 -i rna.h5ad -s spatial.h5ad -o integrated.h5ad`
**Explanation:** `-t 8` uses 8 threads.
