---
name: jvarkit-wgscoverageplotter
category: formatting
description: Whole genome BAM coverage plotter for visualization.
tags: [jvarkit-wgscoverageplotter, formatting, BAM, coverage, visualization]
author: oxo-call-community
source_url: "http://lindenb.github.io/jvarkit/WGSCoveragePlotter.html"
---

## Concepts

- **Tool Overview**: jvarkit-wgscoverageplotter (v20201223) - Plots whole genome coverage from BAM files.
- **Coverage Visualization**: Generates visual representation of sequencing coverage.
- **Whole Genome**: Processes entire genome coverage data.
- **Quality Metrics**: Shows coverage quality across genome.
- **Output Formats**: Supports multiple output formats for plots.
- **Statistics**: Computes coverage statistics alongside visualization.

## Pitfalls

- **BAM Index**: Requires indexed BAM file.
- **Memory Usage**: Whole genome analysis requires significant memory.
- **Plot Size**: High-resolution plots can be large files.
- **Chromosome Order**: Requires proper chromosome ordering.
- **Java Version**: Requires specific Java version.
- **Rendering Time**: Complex plots can take time to generate.

## Examples

### Generate coverage plot
**Args:** `java -jar jvarkit-wgscoverageplotter.jar -i alignments.bam -o coverage.png`
**Explanation:** Generates whole genome coverage plot.

### High resolution output
**Args:** `java -jar jvarkit-wgscoverageplotter.jar -i alignments.bam -o coverage.png -res 300`
**Explanation:** Generates high-resolution plot at 300 DPI.

### Include statistics
**Args:** `java -jar jvarkit-wgscoverageplotter.jar -i alignments.bam -o coverage.png -stats stats.txt`
**Explanation:** Generates coverage statistics alongside plot.

### Specific chromosomes
**Args:** `java -jar jvarkit-wgscoverageplotter.jar -i alignments.bam -o coverage.png -chr chr1 chr2 chr3`
**Explanation:** Plots coverage for specific chromosomes only.

### Custom colors
**Args:** `java -jar jvarkit-wgscoverageplotter.jar -i alignments.bam -o coverage.png -colors blue,red,green`
**Explanation:** Uses custom color scheme for plot.

### PDF output
**Args:** `java -jar jvarkit-wgscoverageplotter.jar -i alignments.bam -o coverage.pdf`
**Explanation:** Outputs plot in PDF format.