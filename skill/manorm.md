---
name: manorm
category: epigenomics
description: A robust model for quantitative comparison of ChIP-Seq data sets.
tags: [manorm, epigenomics, ChIP-seq, normalization]
author: oxo-call-community
source_url: "https://github.com/shao-lab/MAnorm"
---

## Concepts

- **Tool Overview**: manorm v1.3.0 - MAnorm is a robust model for quantitative comparison of ChIP-seq data sets across multiple samples.
- **Core Function**: Normalizes and compares ChIP-seq signal intensities to identify differentially bound regions.
- **Input/Output**: Input: Peak files (BED), signal tracks; Output: Normalized signals, differential binding scores.
- **Installation**: `conda install -c bioconda manorm`
- **Quantitative Comparison**: Uses robust statistical models for comparing signal intensities.
- **Multiple Samples**: Supports comparison of multiple ChIP-seq samples simultaneously.

## Pitfalls

- **Input Quality**: Poor quality peaks affect normalization accuracy.
- **Peak Calling**: Requires consistent peak calling across samples.
- **Coverage**: Low coverage regions may produce unreliable results.
- **Biological Variation**: Biological replicates should be used for reliable comparisons.
- **Parameter Selection**: Incorrect parameters affect statistical significance.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Basic normalization
**Args:** `manorm sample1_peaks.bed sample2_peaks.bed -o results/`
**Explanation:** Normalizes and compares two ChIP-seq samples.

### With signal files
**Args:** `manorm sample1_peaks.bed sample2_peaks.bed -s sample1_signal.bw sample2_signal.bw -o results/`
**Explanation:** Uses BigWig signal files for normalization.

### Multiple samples
**Args:** `manorm sample1.bed sample2.bed sample3.bed -o results/`
**Explanation:** Compares three ChIP-seq samples.

### With control
**Args:** `manorm sample1.bed sample2.bed -c control.bed -o results/`
**Explanation:** Uses control sample for background normalization.

### Verbose mode
**Args:** `manorm sample1.bed sample2.bed -o results/ -v`
**Explanation:** Provides detailed logging during processing.

### Generate plot
**Args:** `manorm sample1.bed sample2.bed -o results/ --plot`
**Explanation:** Generates visualization of results.