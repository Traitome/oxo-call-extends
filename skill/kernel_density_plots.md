---
name: kernel_density_plots
category: alignment
description: Python tool for generating SNP density and closest neighbor plots from aligned SNP FASTA files.
tags: [kernel_density_plots, alignment, SNP, visualization, density]
author: oxo-call-community
source_url: "https://github.com/kapurlab/kernel_density_plots"
---

## Concepts

- **Tool Overview**: kernel_density_plots (v0.1) - Generates SNP density and neighbor plots.
- **SNP Density**: Visualizes SNP distribution across sequences.
- **Kernel Density Estimation**: Uses KDE for smooth density plots.
- **Neighbor Analysis**: Analyzes closest neighbor distances.
- **Visualization**: Generates publication-quality plots.
- **FASTA Input**: Works with aligned SNP FASTA files.

## Pitfalls

- **Alignment Quality**: Requires properly aligned sequences.
- **SNP Calling**: Depends on accurate SNP calling.
- **Memory Usage**: Large alignments require memory.
- **Plot Size**: High-resolution plots can be large.
- **Computation Time**: Complex plots may take time.
- **Sequence Length**: Variable lengths affect analysis.

## Examples

### Generate SNP density plot
**Args:** `kernel_density_plots -i snps.fasta -o density.png`
**Explanation:** Generates SNP density plot from aligned FASTA.

### Neighbor distance plot
**Args:** `kernel_density_plots -i snps.fasta -o neighbor.png -t neighbor`
**Explanation:** Generates closest neighbor distance plot.

### High resolution
**Args:** `kernel_density_plots -i snps.fasta -o density.png -d 300`
**Explanation:** Generates 300 DPI high-resolution plot.

### Multiple sequences
**Args:** `kernel_density_plots -i snps.fasta -o plots/ -m`
**Explanation:** Generates plots for each sequence.

### Custom bandwidth
**Args:** `kernel_density_plots -i snps.fasta -o density.png -b 0.5`
**Explanation:** Sets KDE bandwidth to 0.5.

### Output statistics
**Args:** `kernel_density_plots -i snps.fasta -o stats.txt -s`
**Explanation:** Outputs density statistics.