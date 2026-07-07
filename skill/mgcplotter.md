---
name: mgcplotter
category: utility
description: Microbial Genome Circular plotting tool using Circos
tags: [mgcplotter, utility, visualization]
author: oxo-call-community
source_url: "https://github.com/moshi4/MGCplotter/"
---

## Concepts

- **Tool Overview**: MGCplotter v1.0.1 is a microbial genome circular visualization tool using Circos.
- **Core Function**: Generates circular plots of microbial genomes.
- **Circos Integration**: Uses Circos for high-quality circular visualization.
- **Genome Visualization**: Displays genomic features in circular format.
- **Input/Output**: Accepts genome annotations; outputs circular plots.
- **Multi-feature Display**: Supports visualization of multiple genomic features.

## Pitfalls

- **Circos Dependency**: Requires Circos installation.
- **Computational Resources**: Generating complex plots may require significant resources.
- **Memory Requirements**: Memory usage can be high for large genomes.
- **Parameter Tuning**: May require parameter adjustment for optimal visualization.
- **Data Quality**: Plot quality depends on input annotation quality.
- **Runtime**: Complex plots can be time-consuming to generate.

## Examples

### Generate circular plot
**Args:** `mgcplotter -i genome.gff -o circular_plot.png`
**Explanation:** Generates circular plot of microbial genome.

### With custom configuration
**Args:** `mgcplotter -i genome.gff -o plot.png -c config.conf`
**Explanation:** Uses custom Circos configuration file.

### Multiple features
**Args:** `mgcplotter -i genome.gff -f features.txt -o plot.png`
**Explanation:** Displays multiple genomic features.

### High resolution output
**Args:** `mgcplotter -i genome.gff -o plot.png -r 300`
**Explanation:** Generates high-resolution plot (300 DPI).

### Batch processing
**Args:** `mgcplotter -i genomes/ -o plots/`
**Explanation:** Processes multiple genomes in batch mode.