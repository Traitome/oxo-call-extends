---
name: foci-3d
category: expression
description: FOCI-3D tools for Micro-C transcription factor footprint analysis.
tags: [foci-3d, Micro-C, transcription factor, footprinting, chromatin]
author: oxo-call-community
source_url: "https://github.com/aryeelab/foci-3d"
---

## Concepts
- **Micro-C Footprinting**: Analyzes transcription factor binding sites from Micro-C sequencing data.
- **3D Chromatin Interactions**: Integrates Hi-C style chromatin interaction data with footprinting analysis.
- **TF Binding Detection**: Identifies transcription factor binding events through characteristic footprint patterns.
- **Nucleosome Positioning**: Uses MNase digestion patterns to infer nucleosome positions.
- **Interaction Footprints**: Detects how TF binding affects chromatin interactions in 3D space.

## Pitfalls
- **Micro-C Specific**: Requires Micro-C or similar MNase-based Hi-C data; not compatible with standard Hi-C.
- **Data Quality**: Footprint detection is highly sensitive to MNase digestion quality.
- **TF Database Dependencies**: Relies on known TF binding motifs for prediction.
- **Computational Requirements**: Analyzing genome-wide interactions is computationally intensive.
- **Interpretation Complexity**: Results require careful interpretation considering both sequence and 3D context.

## Examples
### Call footprints from Micro-C data
**Args:** `foci-3d call -i microc.bam -g genome.fa -m motifs.jaspar -o footprints.bed`
**Explanation:** Calls transcription factor footprints from Micro-C BAM file using JASPAR motifs.

### Analyze TF interaction profiles
**Args:** `foci-3d profile -i footprints.bed -c interactions.hic -o tf_interactions.txt`
**Explanation:** Analyzes how TF footprints correlate with chromatin interactions.

### Footprint visualization
**Args:** `foci-3d plot -i footprints.bed -g genome.fa -o footprint_plot.pdf`
**Explanation:** Generates visualization of detected footprints across the genome.

### Differential footprinting analysis
**Args:** `foci-3d diff -i sample1.bed sample2.bed -o diff_footprints.txt`
**Explanation:** Identifies differentially occupied footprints between two samples.

### Motif enrichment analysis
**Args:** `foci-3d enrich -i footprints.bed -m motifs.jaspar -o enrichment.txt`
**Explanation:** Performs motif enrichment analysis on detected footprints.