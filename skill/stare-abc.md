---
name: stare-abc
category: gene-regulation
description: Calculate Gene-TF affinities via enhancer-gene interactions.
tags: [stare-abc, gene-regulation, transcription-factors, enhancers]
author: oxo-call-community
source_url: "https://github.com/SchulzLab/STARE"
---

## Concepts

- **Tool Overview**: stare-abc (v1.0.5) is a tool for calculating transcription factor (TF) affinities to genes based on enhancer-gene interactions.
- **Core Function**: Integrates chromatin accessibility, TF binding motifs, and enhancer-gene links to predict TF-gene regulatory relationships.
- **Algorithm**: Uses ABC (Activity-by-Contact) model to score TF-gene interactions based on enhancer activity and contact frequency.
- **Input/Output**: Input: ATAC-seq peaks, TF motifs, enhancer-gene links; Output: TF-gene affinity scores.
- **Applications**: Gene regulatory network analysis, identifying key transcription factors in gene expression.
- **Installation**: `conda install -c bioconda stare-abc` or download from GitHub.

## Pitfalls

- **Enhancer Quality**: Poor quality enhancer annotations affect affinity calculations.
- **Motif Database**: Outdated or incomplete TF motif databases miss potential interactions.
- **Contact Data**: Requires high-quality Hi-C or similar contact data for accurate predictions.
- **Threshold Selection**: Incorrect threshold settings affect regulatory network inference.
- **Cell Type Specificity**: TF affinities are cell type specific; using wrong cell type data produces incorrect results.
- **Memory Requirements**: Large datasets may require significant memory.

## Examples

### Display help
**Args:** `stare-abc --help`
**Explanation:** Shows available options and usage information.

### Basic affinity calculation
**Args:** `stare-abc -a peaks.bed -m motifs.pwm -l links.txt -o affinities.txt`
**Explanation:** Calculate TF-gene affinities from ATAC-seq peaks and motifs.

### With Hi-C data
**Args:** `stare-abc -a peaks.bed -m motifs.pwm -l links.txt -c hic.cool -o affinities.txt`
**Explanation:** Incorporate Hi-C contact data for better predictions.

### Custom motif database
**Args:** `stare-abc -a peaks.bed -m custom_motifs.pwm -l links.txt -o affinities.txt`
**Explanation:** Use custom TF motif database.

### Output network
**Args:** `stare-abc -a peaks.bed -m motifs.pwm -l links.txt -o network.tsv --network`
**Explanation:** Output TF-gene regulatory network.

### Quality filtering
**Args:** `stare-abc -a peaks.bed -m motifs.pwm -l links.txt -o affinities.txt -q 0.8`
**Explanation:** Filter low-quality predictions with confidence below 0.8.

### Verbose mode
**Args:** `stare-abc -a peaks.bed -m motifs.pwm -l links.txt -o affinities.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Generate visualization
**Args:** `stare-abc -a peaks.bed -m motifs.pwm -l links.txt -o plot.png --plot`
**Explanation:** Generate heatmap of TF-gene affinities.

### Batch processing
**Args:** `stare-abc -a batch/ -m motifs.pwm -l links.txt -o results/`
**Explanation:** Process multiple ATAC-seq datasets.
