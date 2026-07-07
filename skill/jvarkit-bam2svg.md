---
name: jvarkit-bam2svg
category: formatting
description: Converts BAM alignment files to Scalar Vector Graphics (SVG) format.
tags: [jvarkit-bam2svg, formatting, BAM, SVG, visualization]
author: oxo-call-community
source_url: "http://lindenb.github.io/jvarkit/BamToSVG.html"
---

## Concepts

- **Tool Overview**: jvarkit-bam2svg (v201904251722) - Converts BAM alignment files to SVG visualization format.
- **BAM to SVG**: Converts sequence alignments to scalable vector graphics.
- **Visualization**: Generates visual representation of alignments.
- **Region Selection**: Supports visualization of specific genomic regions.
- **Quality Display**: Shows alignment quality information.
- **Java Tool**: Part of the jvarkit Java tool suite.

## Pitfalls

- **Java Dependencies**: Requires Java runtime environment.
- **Memory Usage**: Large BAM files require significant memory.
- **SVG Size**: Complex alignments can produce large SVG files.
- **Region Limits**: Very large regions may not render properly.
- **BAM Index**: Requires indexed BAM file for region queries.
- **Rendering Time**: Complex visualizations can be slow to generate.

## Examples

### Convert BAM to SVG
**Args:** `java -jar jvarkit-bam2svg.jar -i alignments.bam -o output.svg`
**Explanation:** Converts entire BAM file to SVG visualization.

### Specific region
**Args:** `java -jar jvarkit-bam2svg.jar -i alignments.bam -R chr1:1000-2000 -o region.svg`
**Explanation:** Visualizes specific genomic region.

### Include quality
**Args:** `java -jar jvarkit-bam2svg.jar -i alignments.bam -o output.svg -quality`
**Explanation:** Includes quality information in visualization.

### Simplified output
**Args:** `java -jar jvarkit-bam2svg.jar -i alignments.bam -o output.svg -simple`
**Explanation:** Generates simplified SVG output.

### Custom colors
**Args:** `java -jar jvarkit-bam2svg.jar -i alignments.bam -o output.svg -colors custom.txt`
**Explanation:** Uses custom color scheme.

### Filter reads
**Args:** `java -jar jvarkit-bam2svg.jar -i alignments.bam -o output.svg -mapq 30`
**Explanation:** Only includes reads with mapping quality >= 30.