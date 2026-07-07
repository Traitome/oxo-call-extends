---
name: cgview
category: visualization
description: Java package for generating high-quality, zoomable circular genome maps
tags: [cgview, genome-visualization, circular-maps, java, bioinformatics]
author: oxo-call-community
source_url: "http://wishart.biology.ualberta.ca/cgview/"
---

## Concepts

- **Tool Overview**: CGView is a Java package for generating high-quality, interactive circular genome maps suitable for web display.
- **Core Function**: Creates visual representations of circular genomes with annotated features.
- **Features**: Interactive zooming, customizable colors, gene annotations, and web-ready output.
- **Input**: GenBank, EMBL, or GFF annotation files with genome sequence.
- **Output**: Interactive SVG/HTML maps and static image files.
- **Application**: Genome visualization, sequence annotation pipelines, and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cgview`

## Pitfalls

- **Java Dependencies**: Requires Java Runtime Environment.
- **Memory Usage**: Large genomes may require increased heap space.
- **Annotation Format**: Requires specific input format for annotations.
- **Web Server**: Interactive features require web server hosting.

## Examples

### Generate circular genome map
**Args:** `cgview -i genome.gb -o genome_map.html`
**Explanation:** Creates interactive circular map from GenBank file.

### With custom colors
**Args:** `cgview -i genome.gb -o genome_map.html --colors custom_colors.txt`
**Explanation:** Uses custom color scheme for genome features.

### Generate static image
**Args:** `cgview -i genome.gb -o genome_map.png --format png`
**Explanation:** Outputs static PNG image instead of interactive HTML.

### Display help
**Args:** `cgview --help`
**Explanation:** Shows all available options and usage information.