---
name: bam2plot
category: formatting
description: bam2plot - Plot coverage visualization from BAM alignment files
tags: [bam2plot, formatting, BAM, coverage-plot, visualization]
author: oxo-call-community
source_url: "https://github.com/willros/bam2plot"
---

## Concepts

- **Tool Overview**: bam2plot generates coverage plots from BAM alignment files, providing visual representation of sequencing depth across genomic regions. Version 0.4.1.
- **Core Function**: Creates coverage plots and statistics from BAM files for quality assessment.
- **Coverage Visualization**: Generates graphical representations of sequencing coverage.
- **Statistics Calculation**: Computes coverage statistics including mean, median, and percentiles.
- **Region Focus**: Supports plotting specific genomic regions of interest.
- **Input/Output**: Accepts BAM files, outputs coverage plots in various image formats.
- **Installation**: `conda install -c bioconda bam2plot`.

## Pitfalls

- **BAM Index Required**: Requires indexed BAM file for efficient region queries.
- **Memory Usage**: Large BAM files may require significant memory.
- **Output Size**: High-resolution plots can produce large image files.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Basic coverage plot
**Args:** `bam2plot -i alignments.bam -o coverage.png`
**Explanation:** Generates coverage plot from BAM file.

### Plot specific region
**Args:** `bam2plot -i alignments.bam -r chr1:1000-5000 -o region_coverage.png`
**Explanation:** Plots coverage for specified genomic region.

### Multiple BAM comparison
**Args:** `bam2plot -i sample1.bam sample2.bam -o comparison.png`
**Explanation:** Compares coverage across multiple samples.

### Generate statistics
**Args:** `bam2plot -i alignments.bam -s stats.txt -o coverage.png`
**Explanation:** Outputs coverage statistics to text file.

### Custom resolution
**Args:** `bam2plot -i alignments.bam -o coverage.png --dpi 300`
**Explanation:** Generates high-resolution plot at 300 DPI.

### Output PDF format
**Args:** `bam2plot -i alignments.bam -o coverage.pdf --format pdf`
**Explanation:** Outputs plot in PDF format.

### Log scale coverage
**Args:** `bam2plot -i alignments.bam -o coverage.png --log-scale`
**Explanation:** Uses logarithmic scale for coverage axis.

### Display help
**Args:** `bam2plot --help`
**Explanation:** Shows all available command-line options and usage information.