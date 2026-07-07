---
name: jupiterplot
category: assembly
description: Circos Assembly Consistency (Jupiter) plot for genome assembly visualization.
tags: [jupiterplot, assembly, visualization, Circos, genomics]
author: oxo-call-community
source_url: "https://github.com/JustinChu/JupiterPlot/blob/1.1/README.md"
---

## Concepts

- **Tool Overview**: jupiterplot (v1.1) - A tool for generating Circos-based assembly consistency plots (Jupiter plots).
- **Circos Visualization**: Uses Circos for circular genome visualization.
- **Assembly Validation**: Validates genome assembly consistency.
- **Synteny Display**: Shows syntenic relationships between sequences.
- **Coverage Display**: Visualizes sequencing coverage across genome.
- **Assembly Comparison**: Compares multiple assemblies or mappings.

## Pitfalls

- **Circos Dependency**: Requires Circos to be installed.
- **Memory Requirements**: Large genomes require significant memory.
- **Configuration Complexity**: Configuring Circos plots can be complex.
- **Rendering Time**: Complex plots can take time to render.
- **File Formats**: Requires specific input file formats.
- **Output Size**: High-resolution images can be large.

## Examples

### Generate Jupiter plot
**Args:** `jupiterplot --assembly assembly.fasta --alignments alignments.bam --output plot.png`
**Explanation:** Generates Jupiter plot from assembly and alignments.

### Compare two assemblies
**Args:** `jupiterplot --assembly1 asm1.fasta --assembly2 asm2.fasta --output comparison.png`
**Explanation:** Generates comparison plot of two assemblies.

### Custom colors
**Args:** `jupiterplot --assembly assembly.fasta --colors colors.txt --output plot.png`
**Explanation:** Uses custom color scheme for plot.

### High resolution output
**Args:** `jupiterplot --assembly assembly.fasta --output plot.png --resolution 300`
**Explanation:** Generates high-resolution image (300 DPI).

### Include coverage track
**Args:** `jupiterplot --assembly assembly.fasta --coverage coverage.bedgraph --output plot.png`
**Explanation:** Adds coverage track to Jupiter plot.

### Generate configuration
**Args:** `jupiterplot --assembly assembly.fasta --generate-config config.txt`
**Explanation:** Generates Circos configuration file for customization.