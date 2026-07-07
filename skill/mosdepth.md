---
name: mosdepth
category: qc
description: Fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing.
tags: [mosdepth, qc, alignment]
author: oxo-call-community
source_url: "https://github.com/brentp/mosdepth"
---

## Concepts

- **Tool Overview**: mosdepth v0.3.13 calculates sequencing depth efficiently.
- **Core Function**: Computes per-base depth from aligned reads.
- **High Performance**: Optimized for speed and memory efficiency.
- **Multi-scale**: Computes depth at various scales (per-base, windows, regions).
- **Coverage Statistics**: Provides coverage statistics and histograms.
- **Input/Output**: Accepts BAM/CRAM files; outputs depth files and plots.

## Pitfalls

- **BAM Required**: Requires aligned reads in BAM or CRAM format.
- **Memory Requirements**: Memory usage depends on BAM size.
- **Parameter Tuning**: May require parameter adjustment for window size.
- **Data Quality**: Results depend on alignment quality.
- **Index Required**: Requires BAM index file.
- **Computational Resources**: Large BAMs may require significant resources.

## Examples

### Compute depth
**Args:** `mosdepth -t 4 output input.bam`
**Explanation:** Computes per-base depth using 4 threads.

### With custom window size
**Args:** `mosdepth -t 4 --by 1000 output input.bam`
**Explanation:** Computes depth in 1000bp windows.

### For targeted regions
**Args:** `mosdepth -t 4 --regions targets.bed output input.bam`
**Explanation:** Computes depth only in target regions.

### Generate histogram
**Args:** `mosdepth -t 4 --hist output.hist output input.bam`
**Explanation:** Generates depth histogram.

### Batch processing
**Args:** `mosdepth -t 4 --parallel 2 output/ input/`
**Explanation:** Processes multiple BAM files.