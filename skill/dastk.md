---
name: dastk
category: epigenomics
description: DAStk - Differential ATAC-seq toolkit
tags: [dastk, epigenomics, ATAC-seq, differential-analysis, chromatin]
author: oxo-call-community
source_url: "https://github.com/Dowell-Lab/DAStk"
---

## Concepts

- **Tool Overview**: dastk (v1.0.1+) is a differential ATAC-seq toolkit for analyzing chromatin accessibility differences between conditions.
- **Core Function**: Identifies differentially accessible regions (DARs) from ATAC-seq data across experimental conditions.
- **Input/Output**: Input: BAM alignments, peak calls. Output: Differential accessibility scores, DAR lists.
- **Algorithm**: Uses statistical testing to identify significant differences in chromatin accessibility.
- **Key Features**: Handles multiple conditions, normalization support, statistical significance testing.
- **Installation**: `conda install -c bioconda dastk`

## Pitfalls

- **Peak Calling**: Requires high-quality peak calls as input.
- **Normalization**: Proper normalization critical for differential analysis.
- **Replication**: Requires biological replicates for statistical testing.
- **Batch Effects**: May need batch effect correction for multi-batch experiments.
- **Filtering**: Low-quality peaks should be filtered before analysis.

## Examples

### Identify differential peaks
**Args:** `dastk diff -t treatment.bam -c control.bam -p peaks.bed -o diff_peaks.txt`
**Explanation:** Identify differentially accessible peaks between treatment and control.

### Multiple conditions
**Args:** `dastk diff -c condition1.bam condition2.bam condition3.bam -p peaks.bed -o results.txt`
**Explanation:** Analyze differential accessibility across multiple conditions.

### Generate visualization
**Args:** `dastk plot -i diff_peaks.txt -o heatmap.png`
**Explanation:** Generate heatmap visualization of differential peaks.
