---
name: footprint
category: epigenomics
description: Pipeline to find transcription factor footprints in ATAC-seq or DNase-seq data.
tags: [footprint, epigenomics, ATAC-seq, DNase-seq, transcription factor]
author: oxo-call-community
source_url: "https://ohlerlab.mdc-berlin.de/software/Reproducible_footprinting_139/"
---

## Concepts
- **TF Footprinting**: Identifies regions protected by transcription factor binding in open chromatin.
- **ATAC-seq/DNase-seq Analysis**: Works with both assay for transposase-accessible chromatin (ATAC-seq) and DNase-seq data.
- **Nucleosome Positioning**: Infers nucleosome positions from cleavage patterns.
- **Motif Analysis**: Integrates with transcription factor motif databases for footprint annotation.
- **Differential Footprinting**: Compares footprint patterns between conditions.

## Pitfalls
- **Data Quality**: Requires high-quality sequencing data with sufficient depth.
- **Noise Sensitivity**: Footprint detection is sensitive to background noise.
- **TF Motif Dependence**: Relies on known TF binding motifs for annotation.
- **Cell Type Specificity**: Footprints are cell type and condition specific.
- **False Positives**: May detect false footprints in regions with repetitive sequences.

## Examples
### Basic footprint detection
**Args:** `footprint detect -i atac.bam -g genome.fa -o footprints.bed`
**Explanation:** Detects transcription factor footprints from ATAC-seq data.

### Annotate footprints with motifs
**Args:** `footprint annotate -i footprints.bed -m motifs.jaspar -o annotated.bed`
**Explanation:** Annotates detected footprints with known TF binding motifs.

### Differential footprinting analysis
**Args:** `footprint diff -i sample1.bam sample2.bam -o diff_footprints.txt`
**Explanation:** Identifies differentially occupied footprints between two samples.

### Visualize footprints
**Args:** `footprint plot -i footprints.bed -g genome.fa -o footprint_plot.pdf`
**Explanation:** Generates visualization of detected footprints.

### Footprint statistics
**Args:** `footprint stats -i footprints.bed -o stats.txt`
**Explanation:** Generates statistical summary of detected footprints.