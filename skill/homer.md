---
name: homer
category: chip-seq
description: Software for motif discovery and next generation sequencing analysis, including peak calling, motif analysis, and ChIP-seq processing.
tags: [homer, chip-seq, motif-discovery, peak-calling, epigenomics, transcription-factor, histone-modification]
author: oxo-call-community
source_url: "http://homer.ucsd.edu/homer/index.html"
---

## Concepts

- **Tool Overview**: HOMER (Hypergeometric Optimization of Motif EnRichment, v5.1) is a comprehensive bioinformatics tool suite for analyzing high-throughput sequencing data, particularly ChIP-seq, ATAC-seq, DNase-seq, and RNA-seq. It focuses on motif discovery and peak calling.

- **Peak Calling**: The `findPeaks` program identifies enriched regions (peaks) from sequencing data using various modes: factor mode for transcription factors (narrow peaks), histone mode for broad histone marks, super mode for super enhancers, and groseq mode for transcript identification.

- **Motif Discovery**: `findMotifsGenome.pl` performs de novo motif discovery by extracting sequences around peak centers, building k-mer frequency profiles, and identifying statistically enriched motifs. It compares against known motif databases like JASPAR and HOCOMOCO.

- **Peak Annotation**: `annotatePeaks.pl` annotates peaks by mapping them to genomic features (TSS, exons, introns, promoters, enhancers) and provides functional information including gene symbols, GO annotations, and distance metrics.

- **Tag Directory System**: HOMER uses a structured tag directory format to store aligned sequencing reads, enabling efficient access and processing of ChIP-seq data across multiple samples.

- **Quality Control**: Includes tools for assessing ChIP-seq quality such as tag auto-correlation analysis, cross-correlation plots, and sequencing bias detection.

## Pitfalls

- **Genome Configuration**: HOMER requires proper genome configuration before use. Use `configureHomer.pl` to set up reference genomes and ensure all required annotation files are available.

- **Peak Calling Mode Selection**: Choosing the wrong peak calling mode (factor vs histone) can lead to incorrect results. Factor mode is for sharp peaks (TF binding), histone mode for broad regions.

- **Input Control Requirements**: For reliable peak calling, always provide an input control sample to account for background noise and sequencing biases.

- **Motif Size Selection**: The `-size` parameter is critical for motif discovery. Too small may miss important motifs; too large may introduce noise. Typically 50-200 bp around peak centers.

- **Memory Usage**: Processing large datasets can be memory-intensive. Ensure sufficient RAM, especially when analyzing whole-genome datasets.

- **Repeat Masking**: Consider using `-mask` option to exclude repetitive regions from motif analysis, as they can confound motif discovery with spurious matches.

## Examples

### Create tag directory from aligned reads
**Args:** `makeTagDirectory my_chipseq/ -format sam input.bam`
**Explanation:** Creates a HOMER tag directory from aligned BAM file, storing read positions and enabling efficient downstream analysis.

### Call peaks for transcription factor ChIP-seq
**Args:** `findPeaks my_chipseq/ -style factor -o auto -i input_control/`
**Explanation:** Identifies narrow peaks using factor mode with input control for background normalization. Outputs peaks to my_chipseq/peaks.txt.

### Call peaks for histone modification
**Args:** `findPeaks histone_chipseq/ -style histone -o auto -i input_control/`
**Explanation:** Identifies broad peaks for histone modifications using histone mode, suitable for marks like H3K27me3 or H3K36me3.

### Perform de novo motif discovery
**Args:** `findMotifsGenome.pl peaks.txt hg38 motifs_output/ -size 200 -mask`
**Explanation:** Analyzes peak sequences for enriched motifs using 200bp regions around peak centers, with repeat masking enabled.

### Annotate peaks with genomic features
**Args:** `annotatePeaks.pl peaks.txt hg38 -go -geneOntology > annotated_peaks.txt`
**Explanation:** Annotates peaks with genomic features and performs GO enrichment analysis on nearby genes.

### Analyze ChIP-seq with one command
**Args:** `analyzeChIP-Seq.pl my_chipseq/ hg38 -i input_control/ -focus`
**Explanation:** Runs complete ChIP-seq analysis pipeline including QC, peak calling, motif discovery, and annotation in a single command.

### Compare peaks between samples
**Args:** `mergePeaks peaks1.txt peaks2.txt -venn peaks_venn.txt`
**Explanation:** Merges peaks from two samples and generates Venn diagram statistics to compare overlapping and unique peaks.