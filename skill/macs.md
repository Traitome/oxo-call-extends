---
name: macs
category: epigenomics
description: Model Based Analysis for ChIP-Seq data
tags: [macs, epigenomics, ChIP-seq, peak-calling]
author: oxo-call-community
source_url: "http://liulab.dfci.harvard.edu/MACS/"
---

## Concepts

- **Tool Overview**: macs v1.4.3 is the original Model-based Analysis of ChIP-Seq data tool.
- **Core Function**: Identifies transcription factor binding sites from ChIP-seq data.
- **Statistical Approach**: Uses Poisson distribution to model background and signal.
- **Input/Output**: Input: BED/SAM files; Output: Peak calls in BED format.
- **Installation**: `conda install -c bioconda macs`
- **Key Features**: Original implementation, simple interface, widely cited.

## Pitfalls

- **Deprecated**: Consider using macs2 or macs3 for better performance.
- **Limited Features**: Lacks advanced features of newer versions.
- **Memory Usage**: May require significant memory for large datasets.
- **Computation Time**: Slower than newer versions for large datasets.
- **Parameter Limitations**: Fewer parameters than macs2/macs3.
- **Support**: May have limited support compared to newer versions.

## Examples

### Call peaks
**Args:** `macs14 -t treatment.bed -c control.bed -n output`
**Explanation:** Calls peaks from ChIP-seq data.

### With genome size
**Args:** `macs14 -t treatment.bed -c control.bed -g hs -n output`
**Explanation:** Specifies human genome size for normalization.

### BAM input
**Args:** `macs14 -t treatment.bam -c control.bam -f BAM -n output`
**Explanation:** Uses BAM format input files.

### Broad peaks
**Args:** `macs14 -t treatment.bed -c control.bed --broad -n output`
**Explanation:** Calls broad peaks.

### Shift size
**Args:** `macs14 -t treatment.bed -c control.bed --shift=75 --extsize=150 -n output`
**Explanation:** Sets custom shift and extension size.

### Help documentation
**Args:** `macs14 --help`
**Explanation:** Displays all available options and parameters.