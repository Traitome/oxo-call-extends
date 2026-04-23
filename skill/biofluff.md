---
name: biofluff
category: expression
description: Exploratory analysis and visualization of high-throughput sequencing data
tags: [visualization, chip-seq, rna-seq, heatmaps]
author: oxo-call-community
source_url: "https://github.com/simonvh/fluff"
---

## Concepts
- **Tool Overview**: fluff (biofluff) provides exploratory analysis and visualization tools for high-throughput sequencing data, particularly ChIP-seq and RNA-seq.
- **Visualization**: Generates heatmaps, profile plots, and coverage tracks for genomic regions.
- **Clustering**: Includes hierarchical clustering of genomic regions by signal patterns.
- **Applications**: ChIP-seq peak visualization, RNA-seq expression patterns, epigenomic data exploration.

## Pitfalls
- **Memory Usage**: Large datasets with many regions can consume significant memory for clustering.
- **Input Requirements**: Requires BAM/bigWig coverage files and BED region files.

## Examples
### Create heatmap
**Args:** `fluff heatplot -d signal.bw -r regions.bed -o heatmap.png`
**Explanation:** Creates a heatmap of signal over genomic regions.

### Create profile plot
**Args:** `fluff profile -d signal.bw -r regions.bed -o profile.png`
**Explanation:** Creates average signal profile over regions.

### Cluster and visualize
**Args:** `fluff cluster -d signal.bw -r regions.bed -k 5 -o clustered.png`
**Explanation:** Clusters regions by signal pattern and creates heatmap.
