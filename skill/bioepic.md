---
name: bioepic
category: annotation
description: ChIP-Seq broad peak/domain finder
tags: [chip-seq, peak-calling, broad-peaks, domains]
author: oxo-call-community
source_url: "https://github.com/endrebak/epic"
---

## Concepts
- **Tool Overview**: bioepic is a ChIP-Seq broad peak and domain finder, designed to identify wide regions of enrichment (e.g., histone marks) rather than narrow peaks.
- **Broad Peak Detection**: Optimized for histone modifications and other broad enrichment patterns.
- **Statistical Model**: Uses a negative binomial model for background estimation and enrichment scoring.
- **Applications**: Histone mark analysis, chromatin state identification, regulatory domain detection.

## Pitfalls
- **Control Required**: Requires input/control sample for proper background estimation.
- **Not for Narrow Peaks**: Use MACS2 or similar for transcription factor narrow peak calling.

## Examples
### Call broad peaks
**Args:** `epic -t chip.bam -c input.bam -g hg38 > broad_peaks.bed`
**Explanation:** Calls broad peaks/domains from ChIP-seq data.

### Specify genome size
**Args:** `epic -t chip.bam -c input.bam --genome-size hs > peaks.bed`
**Explanation:** Calls peaks using human genome size for normalization.
