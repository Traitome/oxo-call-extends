---
name: sicer
category: epigenomics
description: SICER - Clustering approach for ChIP-seq enriched domain identification
tags: ["sicer", "epigenomics", "chip-seq", "peak-calling"]
author: oxo-call-community
source_url: "http://home.gwu.edu/~wpeng/Software.htm"
---

## Concepts

- **Tool Overview**: SICER (v1.1) identifies enriched domains from histone modification ChIP-seq data.
- **Core Function**: Detects broad peaks using a clustering approach.
- **Algorithm**: Uses sliding window and clustering for peak detection.
- **Input/Output**: Accepts BED/SAM files and produces peak calls.
- **Epigenomics Analysis**: Focuses on histone modifications and broad peaks.
- **Applications**: ChIP-seq analysis, epigenomics research, and chromatin profiling.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment of parameters.
- **Input Quality**: Results depend on sequencing data quality.
- **Control Sample**: Requires matched control for accurate results.
- **Version Compatibility**: Original SICER is legacy software.
- **Documentation**: Limited documentation available.

## Examples

### Call peaks
**Args:** `sicer treatment.bed control.bed output/ hg19`
**Explanation:** Basic peak calling with treatment, control, output, and genome.

### With window size
**Args:** `sicer -w 200 treatment.bed control.bed output/ hg19`
**Explanation:** `-w 200` window size.

### With gap size
**Args:** `sicer -g 600 treatment.bed control.bed output/ hg19`
**Explanation:** `-g 600` gap size.

### Help command
**Args:** `sicer --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sicer --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sicer -v treatment.bed control.bed output/ hg19`
**Explanation:** `-v` verbose output.

### With FDR
**Args:** `sicer -f 0.01 treatment.bed control.bed output/ hg19`
**Explanation:** `-f 0.01` FDR threshold.
