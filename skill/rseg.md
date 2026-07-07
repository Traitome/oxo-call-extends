---
name: rseg
category: chip-seq
description: RSEG (Regression-based Segmentation) is a ChIP-seq analysis tool for identifying genomic regions and boundaries marked by diffusive histone modification markers such as H3K36me3 and H3K27me3.
tags: ["rseg", "chip-seq", "histone-modification", "segmentation", "genomic-regions", "diffusive-markers"]
author: oxo-call-community
source_url: "https://smithlabresearch.org/software/rseg/"
---

## Concepts

- **Tool Overview**: RSEG (v0.4.9, Smith Lab) is a ChIP-seq analysis tool designed specifically for identifying broad genomic domains marked by diffusive histone modifications like H3K36me3 (transcriptional elongation) and H3K27me3 (polycomb repression). It uses regression-based segmentation to define domain boundaries.
- **Core Function**: Takes aligned ChIP-seq reads (BAM/SAM) and identifies contiguous genomic regions with significant enrichment, along with precise boundary positions. Can work with or without control samples.
- **Algorithm**: Uses a two-step approach: (1) Poisson regression to model read counts across the genome; (2) dynamic programming to segment the genome into regions with similar modification patterns. Handles both sharp and broad peaks.
- **Input Format**: BAM/SAM files of aligned reads, chromosome size file (BED format), optional deadzone file for mappability filtering, optional control BAM for background normalization.
- **Output Format**: BED files of predicted domains and boundaries, statistical significance scores, visualization-ready data. Provides both domain calls and boundary positions.
- **Use Case**: Analyzing histone modification ChIP-seq data, identifying active/inactive chromatin domains, comparing epigenetic states between cell types, detecting differential histone modification regions (DHMRs).

## Pitfalls

- **Requires chromosome size file**: Must provide a genome-specific BED file with chromosome lengths. Pre-built files available for hg18, hg19, mm9, dm3.
- **Deadzone file strongly recommended**: Mappability deadzones prevent false positives in repetitive regions. Use pre-computed deadzone files matching read length and genome build.
- **Memory intensive for large genomes**: Full human genome analysis may require ≥16GB RAM. Consider chromosome-by-chromosome analysis for resource-limited environments.
- **Strand information ignored**: RSEG treats reads from both strands identically. Not suitable for strand-specific analyses like transcription factor binding.
- **Parameter sensitivity**: Domain detection thresholds (-w, -q) require tuning based on data quality. Defaults work well for typical histone modification datasets.
- **Control sample recommended but optional**: While RSEG works without controls, normalization improves results, especially for noisy data or low-coverage experiments.

## Examples

### Basic domain calling with control
**Args:** `rseg -i chip.bam -c control.bam -g hg19.chrom.sizes -d deadzones-k36-hg19.bed -o output_prefix`
**Explanation:** `-i` input ChIP BAM, `-c` control BAM, `-g` chromosome sizes, `-d` deadzone file, `-o` output prefix. Generates domains and boundaries in BED format.

### Call domains without control
**Args:** `rseg -i chip.bam -g hg19.chrom.sizes -d deadzones-k36-hg19.bed -o output_prefix --no-control`
**Explanation:** `--no-control` skips control normalization. Use when no control is available, but results may be noisier.

### Identify differential histone modification regions
**Args:** `rseg-diff -i1 chip1.bam -i2 chip2.bam -g hg19.chrom.sizes -o diff_output`
**Explanation:** `rseg-diff` compares two ChIP-seq samples to identify regions with significantly different modification levels. Outputs DHMRs with fold change and p-values.

### Adjust domain width threshold
**Args:** `rseg -i chip.bam -g hg19.chrom.sizes -w 5000 -o output_prefix`
**Explanation:** `-w 5000` sets minimum domain width to 5000bp. Smaller values detect finer domains but increase false positives.

### Run on specific chromosomes
**Args:** `rseg -i chip.bam -g chr1.size -d deadzones-k36-hg19-chr1.bed -o chr1_output`
**Explanation:** Process individual chromosomes separately to reduce memory usage. Requires chromosome-specific size and deadzone files.

### Generate visualization data
**Args:** `rseg -i chip.bam -g hg19.chrom.sizes -d deadzones-k36-hg19.bed -o output_prefix --plot`
**Explanation:** `--plot` generates additional files for genome browser visualization (WIG format). Load tracks in UCSC Genome Browser or IGV.