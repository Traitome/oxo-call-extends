---
name: music
category: epigenomics
description: MUltiScale enrIchment Calling for ChIP-Seq Datasets
tags: [music, epigenomics, chip-seq, enrichment, peak-calling, bam]
author: oxo-call-community
source_url: "http://music.gersteinlab.org"
---

## Concepts

- **Tool Overview**: MUSIC (MUltiScale enrIchment Calling) v1.0.0 is a ChIP-Seq analysis tool for detecting enriched regions across multiple scales. Unlike traditional peak callers that assume uniform signal, MUSIC models enrichment at various spatial scales to capture both narrow transcription factor binding sites and broad epigenetic marks.
- **Core Function**: Identifies enriched genomic regions (peaks) in ChIP-Seq data using a multi-scale approach that detects both narrow peaks (e.g., transcription factors) and broad peaks (e.g., histone modifications). Uses wavelet-based signal decomposition.
- **Algorithm**: Employs a statistical framework based on measuring information content at multiple scales. The signal is decomposed using wavelets, and significant enrichment is detected by comparing observed signal to a background model across scales.
- **Input Format**: Accepts sorted and indexed BAM files from ChIP-Seq experiments. Requires paired-end or single-end reads aligned to a reference genome.
- **Output**: Produces BED format files with identified enriched regions, including p-values and q-values for statistical significance. Also outputs signal tracks in bigWig format.
- **Advantage**: Multi-scale detection handles the full spectrum of ChIP-Seq enrichment patterns, from narrow to broad, without requiring users to know the expected peak shape beforehand.

## Pitfalls

- **BAM Sorting Requirement**: Input BAM files must be coordinate-sorted and indexed. Unsorted BAMs will cause errors. Use `samtools sort` before running MUSIC.
- **Background Model**: MUSIC constructs its own background model from the data. Highly heterogeneous landscapes (e.g., low-complexity regions) may affect background estimation.
- **Scale Selection**: While MUSIC explores multiple scales automatically, understanding which scales are significant helps interpret broad vs narrow enrichment.
- **Replicates**: Single-sample analysis is supported, but biological replicates improve reliability. Consider running on each replicate separately and merging peaks.
- **Memory Usage**: Large BAM files (deep sequencing) require substantial memory. Consider chromosome-by-chromosome processing for whole-genome experiments.
- **Strand Handling**: MUSIC handles both single-end and paired-end data, but paired-end provides better positional information for fragment center estimation.

## Examples

### Basic enrichment detection
**Args:** `-i input.bam -o enriched_peaks.bed`
**Explanation:** Standard MUSIC analysis on an input BAM file. Outputs enriched regions in BED format with statistical significance values.

### Specify genome size for binomial test
**Args:** `-i chip.bam -o peaks.bed -g 3000000000`
**Explanation:** The `-g` flag specifies effective genome size (3GB for human). Used for statistical testing to account for search space.

### Paired-end mode
**Args:** `-i paired.bam -o peaks.bed --pe`
**Explanation:** Use `--pe` flag to enable paired-end mode. MUSIC will use fragment centers instead of read positions for better peak estimation.

### Generate bigWig signal track
**Args:** `-i chip.bam -o peaks.bed --bw chip_signal.bw`
**Explanation:** The `--bw` flag outputs a normalized bigWig signal track for visualization in genome browsers like UCSC or IGV.

### Set minimum peak length
**Args:** `-i input.bam -o peaks.bed --min-length 200`
**Explanation:** Filters out peaks shorter than 200bp. Useful for removing artifactual narrow enrichments from the final peak set.
