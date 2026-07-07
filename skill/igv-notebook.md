---
name: igv-notebook
category: formatting
description: Package for embedding the igv.js genome visualization in IPython notebooks.
tags: [igv-notebook, Jupyter, genome visualization, IGV.js]
author: oxo-call-community
source_url: "https://github.com/igvteam/igv-notebook"
---

## Concepts

- **Tool Overview**: igv-notebook enables embedding interactive IGV genome visualization directly in Jupyter notebooks
- **Core Function**: Provides Python API to create and control IGV.js instances within notebook environments
- **Input/Output**: Supports standard genomic data formats via URLs or local files
- **Installation**: `conda install -c bioconda igv-notebook`
- **Key Features**: Interactive genome browser in notebooks, supports multiple tracks, customizable views

## Pitfalls

- **Browser Compatibility**: Requires modern web browser with JavaScript enabled
- **Network Access**: Remote data URLs must be accessible from the notebook environment
- **Notebook Kernel**: Requires active Jupyter kernel with igv-notebook installed
- **Memory Limits**: Complex visualizations may impact notebook performance
- **Version Dependencies**: Compatibility with specific Jupyter and ipywidgets versions

## Examples

### Basic IGV notebook usage
**Args:** `from igv_notebook import IGV; igv = IGV(genome="hg38"); igv`
**Explanation:** Creates an IGV widget displaying the hg38 genome.

### Load a BAM track
**Args:** `igv.load_track({"name": "Alignments", "url": "sample.bam", "indexURL": "sample.bam.bai", "format": "bam"})`
**Explanation:** Adds a BAM alignment track to the IGV view.

### Jump to specific locus
**Args:** `igv.search("chr1:1000000-1001000")`
**Explanation:** Navigates the IGV view to a specific genomic region.

### Add a gene annotation track
**Args:** `igv.load_track({"name": "Genes", "url": "genes.gff", "format": "gff"})`
**Explanation:** Loads a GFF annotation track for gene visualization.

### Export view as PNG
**Args:** `igv.export_svg("view.svg")`
**Explanation:** Exports the current IGV view as an SVG image.
