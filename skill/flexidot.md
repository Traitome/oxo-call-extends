---
name: flexidot
category: utility
description: "Flexidot is a flexible dotplotting tool for visualizing genomic sequence comparisons and self-similarity."
tags: [flexidot, utility, genomics, visualization, dotplot, sequence-comparison, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/flexidot-bio/flexidot"
---

## Concepts
- **Tool Overview**: Flexidot generates dotplots for comparing genomic sequences, identifying repeats, inversions, and rearrangements within or between sequences.
- **Core Function**: Creates visual dotplots showing sequence similarity, repeats, and structural variations in genomic data.
- **Input/Output**: Input: FASTA sequence files. Output: SVG/PDF/PNG dotplot images, optional alignment statistics.
- **Sequence Comparison**: Supports self-comparison (repeat detection) and cross-comparison (homology detection).
- **Dotplot Types**: Generates standard dotplots, diagonal plots, and heatmap-style visualizations.
- **Filtering Options**: Allows filtering by minimum match length, identity threshold, and repeat masking.
- **Installation**: `conda install -c bioconda flexidot` or clone from GitHub. Requires Python 3.x and matplotlib.

## Pitfalls
- **Sequence Size Limits**: Very large sequences (>100kb) may produce cluttered dotplots. Consider subsetting.
- **Memory Requirements**: Full genome comparisons require significant memory. Use chunked processing for large sequences.
- **Repeat Regions**: Highly repetitive sequences (e.g., centromeres) may obscure meaningful signals.
- **Identity Threshold**: Low identity thresholds produce excessive noise. Adjust based on expected similarity.
- **Visualization Resolution**: High-resolution images require significant rendering time. Balance resolution with file size.
- **Sequence Orientation**: Ensure sequences are in correct orientation. Reverse complement sequences for strand-specific comparisons.

## Examples
### Basic self-comparison dotplot
**Args:** `flexidot -i genome.fasta -o dotplot.svg --self`
**Explanation:** Generates dotplot showing self-similarity and repeat regions in the input sequence.

### Compare two sequences
**Args:** `flexidot -i query.fasta -j target.fasta -o comparison.svg`
**Explanation:** Creates dotplot comparing query and target sequences for homology detection.

### With identity filtering
**Args:** `flexidot -i genome.fasta -o dotplot.svg --self --min-identity 90 --min-length 50`
**Explanation:** Filters matches to show only regions with >=90% identity and >=50bp length.

### Generate heatmap style
**Args:** `flexidot -i genome.fasta -o heatmap.svg --self --heatmap`
**Explanation:** Creates heatmap-style dotplot with color intensity representing match density.

### Include repeat masking
**Args:** `flexidot -i genome.fasta -o dotplot.svg --self --mask-repeats --mask-file repeats.bed`
**Explanation:** Masks specified repeat regions to focus on unique sequence comparisons.
