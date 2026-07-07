---
name: snapatac2
category: single-cell
description: SnapATAC2 - Single-cell epigenomics analysis pipeline for ATAC-seq data
tags: [snapatac2, single-cell, epigenomics, atac-seq, chromatin]
author: oxo-call-community
source_url: "https://scverse.org/SnapATAC2"
---

## Concepts

- **Tool Overview**: snapatac2 (v2.9.0) - A comprehensive pipeline for single-cell ATAC-seq analysis
- **Core Function**: Analyzes single-cell chromatin accessibility data
- **Input/Output**: Accepts scATAC-seq data; outputs cell clusters and peak calls
- **Algorithm**: Integrates preprocessing, dimensionality reduction, and clustering
- **Installation**: `conda install -c bioconda snapatac2`
- **Key Features**: Single-cell analysis, peak calling, visualization

## Pitfalls

- **Input Requirements**: Requires properly formatted scATAC-seq data
- **Memory Usage**: Large single-cell datasets require significant memory
- **Computation Time**: Analysis can be computationally intensive
- **Parameter Tuning**: Requires careful parameter adjustment
- **Quality Filtering**: Low-quality cells must be filtered
- **Normalization**: Proper normalization is critical for results

## Examples

### Display help
**Args:** `snapatac2 --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `snapatac2 run -i input.bam -o results/`
**Explanation:** Run basic SnapATAC2 analysis pipeline.

### With reference genome
**Args:** `snapatac2 run -i input.bam -r reference.fasta -o results/`
**Explanation:** Specify reference genome for analysis.

### Quality filtering
**Args:** `snapatac2 run -i input.bam -o results/ --min-fragments 1000`
**Explanation:** Filter cells by minimum fragment count.

### Dimensionality reduction
**Args:** `snapatac2 run -i input.bam -o results/ --n-components 50`
**Explanation:** Set number of components for dimensionality reduction.

### Clustering analysis
**Args:** `snapatac2 run -i input.bam -o results/ --n-clusters 10`
**Explanation:** Specify number of clusters for analysis.

### Peak calling
**Args:** `snapatac2 peaks -i input.bam -o peaks.bed`
**Explanation:** Call peaks from scATAC-seq data.

### Generate report
**Args:** `snapatac2 report -i results/ -o report.html`
**Explanation:** Generate analysis report.