---
name: gopeaks
category: bioinformatics
description: GoPeaks is a fast and sensitive peak caller specifically designed for CUT&TAG and CUT&RUN sequencing data analysis.
tags: [gopeaks, peak-calling, CUT&TAG, CUT&RUN, ChIP-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/maxsonBraunLab/gopeaks"
---

## Concepts

- **Peak Calling**: GoPeaks identifies enriched regions (peaks) in CUT&TAG/CUT&RUN data that indicate protein-DNA binding sites.

- **CUT&TAG Optimization**: Specifically optimized for CUT&TAG data characteristics, including low background and high signal-to-noise ratio.

- **Dual Mode**: Supports both narrow peak calling (for transcription factors) and broad peak calling (for histone modifications).

- **Quality Control**: Includes built-in quality control metrics for assessing peak quality and reproducibility.

- **Fast Processing**: Implemented in Go for high performance, enabling rapid analysis of large sequencing datasets.

- **Reproducibility**: Designed to produce consistent results across biological replicates.

## Pitfalls

- **Input Quality**: Results depend heavily on input data quality. Ensure reads are properly trimmed and filtered.

- **Control Samples**: Always use appropriate control samples for background subtraction to reduce false positives.

- **Peak Width**: Choose appropriate peak width based on the target protein type (narrow for TFs, broad for histones).

- **Threshold Selection**: Adjust significance thresholds based on experimental design and expected signal strength.

- **Memory Usage**: Processing very large datasets may require significant memory. Consider downsampling if needed.

## Examples

### Basic peak calling
**Args:** `gopeaks -i sample.bam -o peaks.bed`
**Explanation:** Calls peaks from CUT&TAG BAM file and outputs results in BED format.

### Broad peak mode
**Args:** `gopeaks -i sample.bam --broad -o broad_peaks.bed`
**Explanation:** Calls broad peaks suitable for histone modifications like H3K4me3 or H3K27ac.

### With control sample
**Args:** `gopeaks -i sample.bam -c control.bam -o peaks.bed`
**Explanation:** Uses control sample for background subtraction to improve peak calling accuracy.

### Adjust significance threshold
**Args:** `gopeaks -i sample.bam -p 0.001 -o peaks.bed`
**Explanation:** Sets a stricter p-value threshold (0.001) for peak calling.

### Specify fragment length
**Args:** `gopeaks -i sample.bam -f 150 -o peaks.bed`
**Explanation:** Sets expected fragment length to 150 base pairs for improved peak detection.

### Generate QC report
**Args:** `gopeaks -i sample.bam --qc -o qc_report.html`
**Explanation:** Generates a quality control report with peak statistics and visualization.

### Batch processing
**Args:** `gopeaks -d samples/ -c control.bam -o peaks/`
**Explanation:** Processes all BAM files in the samples directory and saves individual peak files.