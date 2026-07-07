---
name: dropletutils-scripts
category: programming
description: "CLI scripts for the DropletUtils package"
tags: [dropletutils-scripts, programming, single-cell, RNA-seq, DropletUtils]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/dropletutils-scripts"
---

## Concepts

- **Tool Overview**: dropletutils-scripts provides CLI wrappers for the DropletUtils R package, making its functionality accessible outside of R workflows.
- **Core Function**: Enables command-line access to single-cell RNA-seq analysis functions from DropletUtils.
- **Input/Output**: Input: Gene expression matrices, raw counts. Output: Filtered matrices, QC metrics, cell calls.
- **Algorithm**: Wraps R functions with robust argument parsing for language-agnostic workflow integration.
- **Key Features**: Cell calling, empty droplet detection, quality filtering, language-agnostic intermediate formats.
- **Installation**: `conda install -c bioconda dropletutils-scripts`

## Pitfalls

- **R Dependency**: Requires R and DropletUtils package to be installed.
- **File Format**: Intermediate files may be R-specific formats (RDS).
- **Memory Usage**: Large datasets may require significant memory.
- **Version Compatibility**: Ensure compatibility between script version and DropletUtils version.
- **Output Compatibility**: Some outputs may require R for downstream processing.

## Examples

### Detect empty droplets
**Args:** `emptyDrops --input counts.mtx --output empty_drops.txt`
**Explanation:** Identifies empty droplets from raw count matrix.

### Filter cells
**Args:** `filterCells --input counts.mtx --output filtered.mtx --min-genes 200`
**Explanation:** Filters cells with fewer than 200 detected genes.

### Generate QC metrics
**Args:** `computeQCMetrics --input counts.mtx --output qc.txt`
**Explanation:** Computes quality control metrics for cells.

### Downsample counts
**Args:** `downsampleMatrix --input counts.mtx --output downsampled.mtx --prop 0.5`
**Explanation:** Downsamples count matrix to 50% of original depth.

### Merge matrices
**Args:** `mergeMatrices --inputs counts1.mtx counts2.mtx --output merged.mtx`
**Explanation:** Merges multiple count matrices into one.