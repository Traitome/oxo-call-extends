---
name: cnvkit
category: variant-calling
description: Copy number variant detection from high-throughput sequencing data
tags: [cnvkit, cnv, copy-number, segmentation, ngs, cancer]
author: oxo-call-community
source_url: "https://github.com/etal/cnvkit"
---

## Concepts

- **Tool Overview**: CNVkit is a Python toolkit for copy number variation detection from high-throughput sequencing data, supporting both targeted and whole-genome sequencing.
- **Core Function**: Detects copy number alterations from read depth, segments the genome, and calls CNVs by comparing tumor to normal samples or a reference.
- **Input/Output**: Input: BAM/CRAM files from targeted or whole-genome sequencing. Output: CNV calls (SEG, VCF), copy number profiles, and visualization plots.
- **Reference Building**: Creates a reference from normal samples or uses a flat reference for tumor-only analysis.
- **Segmentation Methods**: Supports multiple segmentation algorithms: circular binary segmentation (CBS), HaarSeg, and others.
- **Batch Mode**: Provides batch processing for multiple samples with automatic reference creation and CNV calling.

## Pitfalls

- **Reference Required**: Need a reference (from normal samples or flat) before calling CNVs. Build reference with `cnvkit.py reference`.
- **Tumor-Normal Pairs**: For best results, use matched normal samples. Tumor-only mode is possible but less accurate.
- **Target vs WGS**: Different parameters for targeted sequencing vs whole-genome. Use `--method wgs` for whole-genome data.
- **Binning Size**: Default bin size works for most cases. Adjust `--bin-size` for different coverage levels.
- **Sex Chromosomes**: Sex chromosomes need special handling. Use `--male-reference` for male samples.
- **GC Bias**: CNVkit corrects for GC bias automatically. Ensure reference includes GC correction.

## Examples

### Build reference from normal samples
**Args:** `reference *.bam -o reference.cnn -f reference.fa`
**Explanation:** Creates a reference from normal sample BAMs for tumor-normal CNV calling.

### Build flat reference for tumor-only
**Args:** `reference -o flat_reference.cnn -f reference.fa --targets targets.bed`
**Explanation:** Creates a flat reference for tumor-only CNV calling when no normal samples available.

### Call CNVs from tumor-normal pair
**Args:** `batch tumor.bam -r reference.cnn -n normal.bam -f reference.fa --output-dir output/`
**Explanation:** Full CNV calling pipeline: bins, corrects, segments, and calls CNVs from tumor-normal pair.

### Call CNVs from tumor-only
**Args:** `batch tumor.bam -r flat_reference.cnn -f reference.fa --output-dir output/`
**Explanation:** Calls CNVs from tumor sample only using a flat reference, less accurate than tumor-normal.

### Process single sample step-by-step
**Args:** `coverage tumor.bam -r reference.cnn -o tumor.cnn`
**Explanation:** Calculates read coverage in bins, first step of manual CNV calling pipeline.

### Correct for biases
**Args:** `fix tumor.cnn reference.cnn -o tumor.cnr`
**Explanation:** Corrects for GC bias and reference bias, producing a copy number ratio file.

### Segment the genome
**Args:** `segment tumor.cnr -o tumor.cns`
**Explanation:** Segments the genome into regions of constant copy number using CBS algorithm.

### Call CNV events
**Args:** `call tumor.cns -o tumor.call.cns`
**Explanation:** Calls copy number alterations from segmented data, assigns integer copy numbers.

### Generate visualization
**Args:** `scatter tumor.cnr tumor.cns -o tumor_scatter.png`
**Explanation:** Creates a scatter plot of copy number ratios with segment boundaries.

### Generate heatmap for multiple samples
**Args:** `heatmap *.cns -o heatmap.png`
**Explanation:** Creates a heatmap showing copy number profiles across multiple samples.

### Export to VCF format
**Args:** `export vcf tumor.call.cns -o tumor.vcf`
**Explanation:** Exports CNV calls in VCF format for compatibility with other tools.

### Export to SEG format
**Args:** `export seg *.cns -o samples.seg`
**Explanation:** Exports segmented copy number data in SEG format for visualization in IGV.
