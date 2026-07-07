---
name: fsnviz
category: utility
description: Tool for plotting gene fusion events detected by various tools using Circos.
tags: [fsnviz, gene fusion, visualization, Circos]
author: oxo-call-community
source_url: "https://github.com/bow/fsnviz"
---

## Concepts
- **Gene Fusion Visualization**: Creates visualizations of gene fusion events.
- **Circos Integration**: Uses Circos for circular genome visualization.
- **Multi-tool Support**: Supports input from various fusion detection tools.
- **Genomic Context**: Shows fusion events in genomic context.
- **Interactive Plots**: Generates publication-quality figures.

## Pitfalls
- **Circos Dependency**: Requires Circos to be installed.
- **Input Format**: Requires specific input format.
- **Output Customization**: Limited customization options.
- **Memory Requirements**: Large datasets require significant memory.
- **Learning Curve**: Requires understanding of Circos configuration.

## Examples
### Basic fusion visualization
**Args:** `fsnviz -i fusions.txt -o fusion_plot.png`
**Explanation:** Generates visualization of fusion events.

### With reference genome
**Args:** `fsnviz -i fusions.txt -g genome.fa -o fusion_plot.png`
**Explanation:** Uses reference genome for context.

### Custom colors
**Args:** `fsnviz -i fusions.txt -c colors.txt -o fusion_plot.png`
**Explanation:** Uses custom color scheme.

### Multiple samples
**Args:** `fsnviz -i sample1.txt sample2.txt -o comparison_plot.png`
**Explanation:** Visualizes fusions from multiple samples.

### High-resolution output
**Args:** `fsnviz -i fusions.txt -o fusion_plot.pdf -r high`
**Explanation:** Generates high-resolution PDF output.