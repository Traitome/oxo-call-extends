---
name: coolpuppy
category: formatting
description: Pile-up analysis on Hi-C data in cooler format
tags: [coolpuppy, hi-c, pile-up, genomics, chromatin-interactions]
author: oxo-call-community
source_url: "https://coolpuppy.readthedocs.io"
---

## Concepts

- **Tool Overview**: coolpuppy is a versatile tool for performing pile-up analysis on Hi-C data stored in .cool format, enabling visualization of average interaction patterns around genomic features.
- **Core Function**: Extracts and aggregates Hi-C contact matrices around specified genomic regions to identify interaction patterns.
- **Algorithm**: Aggregates contact frequencies from Hi-C matrices around user-defined anchor regions.
- **Input**: Cooler files (.cool/.mcool), BED files defining anchor regions.
- **Output**: Pile-up matrices, heatmaps, and statistical summaries of interaction patterns.
- **Application**: Analyzing chromatin interactions, enhancer-promoter contacts, and TAD boundaries.
- **Installation**: Install via bioconda: `conda install -c bioconda coolpuppy`

## Pitfalls

- **Resolution Selection**: Choosing appropriate resolution is critical for meaningful results.
- **Region Size**: Small anchor regions may produce noisy pile-ups.
- **Normalization**: Requires balanced (normalized) Hi-C matrices.
- **Distance Dependence**: Interaction patterns vary with genomic distance.
- **Multiple Testing**: Multiple anchor regions may require statistical correction.

## Examples

### Basic pile-up analysis
**Args:** `coolpuppy call --cooler matrix.mcool::/resolutions/10000 --features anchors.bed -o pileup.npz`
**Explanation:** Generates pile-up around anchor regions from 10kb resolution matrix.

### With flanking region
**Args:** `coolpuppy call --cooler matrix.mcool --features anchors.bed --flank 50000 -o pileup.npz`
**Explanation:** Includes 50kb flanking regions around anchors.

### Plot pile-up heatmap
**Args:** `coolpuppy plot pileup.npz -o heatmap.png`
**Explanation:** Generates visualization of the pile-up matrix.

### Multiple feature sets
**Args:** `coolpuppy call --cooler matrix.mcool --features set1.bed set2.bed -o combined_pileup.npz`
**Explanation:** Compares pile-up patterns across multiple feature sets.

### Display help
**Args:** `coolpuppy --help`
**Explanation:** Shows all available options and usage information.