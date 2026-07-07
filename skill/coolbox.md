---
name: coolbox
category: utility
description: Jupyter-based genomic data visualization toolkit
tags: [coolbox, visualization, genomics, jupyter, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/GangCaoLab/CoolBox"
---

## Concepts

- **Tool Overview**: CoolBox is a Jupyter notebook based genomic data visualization toolkit that provides interactive visualization of genomic tracks.
- **Core Function**: Visualizes various genomic data types including Hi-C contact maps, ChIP-seq signals, gene annotations, and variant data.
- **Algorithm**: Uses matplotlib and HiGlass for rendering interactive genomic visualizations in Jupyter notebooks.
- **Input**: Genomic data files (BED, BigWig, BAM, Cooler, GFF, VCF, etc.).
- **Output**: Interactive plots and visualizations within Jupyter notebooks.
- **Application**: Genomic data exploration, publication-quality figure generation, and data sharing.
- **Installation**: Install via bioconda: `conda install -c bioconda coolbox`

## Pitfalls

- **Jupyter Dependencies**: Requires Jupyter environment for interactive features.
- **Memory Usage**: Large datasets may require significant memory.
- **Browser Compatibility**: Interactive features depend on browser support.
- **Rendering Time**: Complex plots may take time to render.
- **Data Preprocessing**: Some formats require preprocessing (e.g., Hi-C matrices).

## Examples

### Basic track visualization
**Args:** `from coolbox.api import *; Track("signal.bw").plot("chr1:1-1000000")`
**Explanation:** Plots a BigWig track in Jupyter notebook.

### Multi-track visualization
**Args:** `Frame() + Track("genes.gff") + Track("peaks.bed") + Track("signal.bw")`
**Explanation:** Creates composite visualization with multiple tracks.

### Hi-C matrix visualization
**Args:** `HiCTrack("matrix.cool").plot("chr1", "chr1")`
**Explanation:** Visualizes Hi-C contact matrix.

### Save to file
**Args:** `frame = Frame() + Track("signal.bw"); frame.save("output.png")`
**Explanation:** Saves visualization to image file.