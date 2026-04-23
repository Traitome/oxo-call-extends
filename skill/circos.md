---
name: circos
category: utility
description: Circular visualization of genomic data and information
tags: [circos, visualization, circular-plot, genomics, sv, cnv]
author: oxo-call-community
source_url: "http://circos.ca"
---

## Concepts

- **Tool Overview**: Circos is a software package for visualizing data and information in a circular layout, widely used for genomic data visualization including structural variations, copy number variations, and comparative genomics.
- **Core Function**: Generates publication-quality circular plots from configuration files, ideal for showing relationships between genomic positions (e.g., translocations, fusions).
- **Input/Output**: Input: Configuration files (.conf) and data files (karyotype, links, histograms, etc.). Output: PNG, SVG, or PDF images.
- **Configuration-Driven**: All visual elements are defined in configuration files with extensive customization options for colors, fonts, spacing, and data tracks.
- **Data Tracks**: Supports multiple track types: scatter, line, histogram, heatmap, text, connectors, links, highlights, and ribbons.
- **Helper Tools**: Includes utilities like `parse-table`, `grep`, `bins`, and `tableviewer` for data manipulation.

## Pitfalls

- **Configuration Complexity**: Circos configuration is extensive. Start from example templates rather than from scratch.
- **Karyotype Required**: Must define chromosome names, lengths, and colors in a karyotype file before any visualization.
- **Coordinate System**: Uses 0-based coordinates. Ensure your data matches this convention.
- **Memory Usage**: Large datasets (whole-genome links) can consume significant memory. Use `chromosomes` parameter to limit scope.
- **Font Issues**: May require specific TrueType fonts. Install `libpng` and `freetype` dependencies.
- **SVG Output**: SVG output can be very large for complex plots. Use PNG for quick previews and SVG/PDF for publication.

## Examples

### Basic Circos plot
**Args:** `-conf circos.conf -outputdir output/`
**Explanation:** Generates a Circos plot from the main configuration file, outputting to the specified directory.

### Generate PNG output
**Args:** `-conf circos.conf -outputdir output/ -png`
**Explanation:** Produces PNG format output, suitable for quick previews and presentations.

### Generate SVG output
**Args:** `-conf circos.conf -outputdir output/ -svg`
**Explanation:** Produces SVG format output for publication-quality vector graphics that can be edited in Illustrator.

### Limit to specific chromosomes
**Args:** `-conf circos.conf -outputdir output/ -chromosomes chr1,chr2,chr3`
**Explanation:** Only draws the specified chromosomes, useful for focused analysis or reducing plot complexity.

### Show only a region
**Args:** `-conf circos.conf -outputdir output/ -chromosomes chr1:10000000-50000000`
**Explanation:** Zooms into a specific region of chr1 (10Mb-50Mb), useful for detailed local visualization.

### Debug configuration
**Args:** `-conf circos.conf -debug_group text,rule`
**Explanation:** Enables debug output for text and rule processing, helpful for troubleshooting configuration issues.

### Validate configuration without generating image
**Args:** `-conf circos.conf -nop`
**Explanation:** Validates the configuration file without generating the image, useful for catching errors quickly.

### Generate with custom image size
**Args:** `-conf circos.conf -outputdir output/ -radius 2000p`
**Explanation:** Sets the image radius to 2000 pixels for high-resolution output suitable for large posters.
