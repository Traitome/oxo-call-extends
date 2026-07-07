---
name: jamm
category: epigenomics
description: JAMM is a peak finder for NGS datasets (ChIP-Seq, ATAC-Seq, DNase-Seq) that integrates replicates and assigns peak boundaries accurately.
tags: [jamm, epigenomics, peak-calling, ChIP-Seq, ATAC-Seq]
author: oxo-call-community
source_url: "https://github.com/mahmoudibrahim/JAMM"
---

## Concepts

- **Tool Overview**: jamm (v1.0.8.0) - A robust peak caller for epigenomics data that combines biological replicates and accurately defines peak boundaries.
- **Replicate Integration**: Combines multiple biological replicates to improve peak detection reliability.
- **Boundary Detection**: Uses a two-step approach to accurately define peak boundaries.
- **False Discovery Rate**: Implements FDR-based filtering for reliable peak calling.
- **Control Sample Support**: Incorporates control/input samples for background normalization.
- **Multi-sample Analysis**: Supports simultaneous analysis of multiple samples.

## Pitfalls

- **Replicate Variability**: High variability between replicates can affect integration.
- **Input Quality**: Poor quality control samples can lead to false positives.
- **Peak Overlap**: Overlapping peaks from different factors may be merged incorrectly.
- **Threshold Selection**: Choosing appropriate thresholds requires careful consideration.
- **Chromosome Artifacts**: Centromeric and telomeric regions may produce false peaks.
- **Memory Requirements**: Large datasets require significant memory for processing.

## Examples

### Call peaks from ChIP-Seq
**Args:** `jamm -i chip.bam -c input.bam -o peaks/`
**Explanation:** Calls peaks using ChIP and input control BAM files.

### Multiple replicates
**Args:** `jamm -i rep1.bam rep2.bam -c input.bam -o peaks/`
**Explanation:** Integrates multiple biological replicates for peak calling.

### Set FDR threshold
**Args:** `jamm -i chip.bam -c input.bam -o peaks/ -f 0.01`
**Explanation:** Sets FDR threshold to 1% for peak filtering.

### Adjust peak width
**Args:** `jamm -i chip.bam -c input.bam -o peaks/ -w 200`
**Explanation:** Sets expected peak width to 200 bp.

### Output narrow peaks
**Args:** `jamm -i chip.bam -c input.bam -o peaks/ --narrow`
**Explanation:** Outputs narrow peak calls suitable for transcription factor binding sites.

### Include blacklist regions
**Args:** `jamm -i chip.bam -c input.bam -o peaks/ --blacklist blacklist.bed`
**Explanation:** Excludes blacklist regions from peak calling.