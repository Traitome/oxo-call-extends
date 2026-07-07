---
name: asciigenome
category: assembly
description: Asciigenome - ASCII-based command-line genome browser
tags: [asciigenome, assembly, genome-browser, terminal, visualization]
author: oxo-call-community
source_url: "https://asciigenome.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: Asciigenome is a command-line genome browser that runs entirely in the terminal using ASCII characters for visualization. Version 1.20.0.
- **Core Function**: Provides interactive genome browsing and annotation viewing directly from terminal without requiring graphical interface.
- **ASCII Visualization**: Uses ASCII characters to display genomic features, tracks, and annotations in terminal window.
- **Terminal-Based**: Runs entirely in command-line interface. Suitable for remote servers and headless environments.
- **Feature Display**: Shows genes, exons, introns, and other genomic features in scrollable format.
- **Navigation**: Supports keyboard navigation for browsing genome regions and zooming in/out.
- **Input/Output**: Accepts GFF/GFF3 annotation files and reference genomes.
- **Installation**: `conda install -c bioconda asciigenome` or install from PyPI.

## Pitfalls

- **Terminal Size**: Requires minimum terminal dimensions for proper display. Small terminals may truncate content.
- **Color Support**: Some terminals may not support colors used for feature highlighting.
- **Large Genomes**: Very large genomes may be slow to load and navigate.
- **Annotation Format**: Requires properly formatted GFF/GFF3 files. Incorrect formats cause parsing errors.
- **Resolution**: ASCII representation has limited resolution compared to graphical browsers.
- **Unicode Support**: Some ASCII characters may not display correctly on all terminals.

## Examples

### Display help
**Args:** `asciigenome --help`
**Explanation:** Shows all available command-line options and usage information.

### Browse genome with annotations
**Args:** `asciigenome --genome genome.fasta --annotations genes.gff`
**Explanation:** Launches ASCII genome browser with reference genome and gene annotations. Interactive terminal interface for browsing.

### Specify chromosome
**Args:** `asciigenome --genome genome.fasta --annotations genes.gff --chr chr1`
**Explanation:** Opens browser for specific chromosome (chr1). Faster loading for large genomes.

### Set start position
**Args:** `asciigenome --genome genome.fasta --annotations genes.gff --start 1000000`
**Explanation:** Opens browser at specified genomic position (1,000,000bp). Useful for quick navigation to region of interest.

### Set window size
**Args:** `asciigenome --genome genome.fasta --annotations genes.gff --window 5000`
**Explanation:** Sets display window size to 5,000bp. Controls amount of genomic context shown.

### Show specific feature types
**Args:** `asciigenome --genome genome.fasta --annotations genes.gff --features gene,exon`
**Explanation:** Displays only gene and exon features. Filters out other annotation types.

### Enable color highlighting
**Args:** `asciigenome --genome genome.fasta --annotations genes.gff --color`
**Explanation:** Enables color highlighting for different feature types. Requires color-capable terminal.

### Export current view
**Args:** `asciigenome --genome genome.fasta --annotations genes.gff --export view.txt`
**Explanation:** Exports current ASCII view to text file. Useful for documentation or sharing.