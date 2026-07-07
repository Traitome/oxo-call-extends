---
name: strudel
category: visualization
description: Strudel is a graphical tool for visualizing genetic and physical maps of genomes for comparative purposes.
tags: [strudel, genome-visualization, genetic-maps, comparative-genomics]
author: oxo-call-community
source_url: "https://ics.hutton.ac.uk/strudel"
---

## Concepts

- **Tool Overview**: strudel (v1.15.08.25) is a graphical tool for visualizing genetic and physical maps of genomes for comparative purposes.
- **Core Function**: Visualizes genetic and physical maps for comparative genomics analysis.
- **Algorithm**: Uses graphical rendering to display genome maps with annotations.
- **Input/Output**: Input: Genetic/physical map files; Output: Interactive visualization.
- **Applications**: Comparative genomics, genome mapping, genetic analysis.
- **Installation**: `conda install -c bioconda strudel` or download from website.

## Pitfalls

- **Input Format**: Requires specific map file format.
- **Memory Requirements**: Large genome maps require significant memory.
- **Visualization Complexity**: Very large maps may be hard to visualize.
- **Interactive Performance**: May be slow with very large datasets.
- **Export Limitations**: Export options may be limited for complex visualizations.
- **Coordinate System**: Requires consistent coordinate system.

## Examples

### Display help
**Args:** `strudel --help`
**Explanation:** Shows available options and usage information.

### Basic map visualization
**Args:** `strudel -i map.gff -o map.svg`
**Explanation:** Visualize genetic map from GFF file.

### With physical map
**Args:** `strudel -i genetic.gff -p physical.gff -o comparison.svg`
**Explanation:** Compare genetic and physical maps.

### Verbose mode
**Args:** `strudel -i map.gff -o map.svg -v`
**Explanation:** Run with detailed logging for debugging.

### Output multiple formats
**Args:** `strudel -i map.gff -o map --formats svg pdf png`
**Explanation:** Output visualization in multiple formats.

### Batch processing
**Args:** `strudel -i maps/ -o results/`
**Explanation:** Process multiple map files together.

### Filter by chromosome
**Args:** `strudel -i map.gff -o map.svg -c chr1`
**Explanation:** Visualize specific chromosome.

### Include annotations
**Args:** `strudel -i map.gff -a annotations.gff -o map.svg`
**Explanation:** Include additional annotations in visualization.

### Generate report
**Args:** `strudel -i map.gff -o map.svg --report`
**Explanation:** Generate comprehensive HTML report.
