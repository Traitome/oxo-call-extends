---
name: alignoth
category: alignment
description: Create portable alignment plots from BAM files with interactive HTML and Vega-Lite output
tags: [alignoth, alignment-visualization, BAM, vega-lite, HTML, visualization]
author: oxo-call-community
source_url: "https://github.com/alignoth/alignoth"
---

## Concepts

- **Tool Overview**: Alignoth is a lightweight command-line application for creating portable alignment plots from BAM files, generating self-contained HTML reports and Vega-Lite specifications.
- **Core Function**: Visualizes DNA sequencing read alignments with support for interactive HTML output, static image formats (PNG, SVG, PDF), and embeddable JSON representations.
- **Output Formats**: Vega-Lite JSON specification (default), interactive HTML, static images via vega-cli.
- **Features**: Read name search, mapping-quality-based read highlighting, paired-end read visualization, customizable region selection.
- **Interactive Mode**: Launch wizard mode by running `alignoth` without arguments for guided plot creation.
- **Installation**: Install via bioconda: `conda install -c bioconda alignoth` or via cargo: `cargo install alignoth`
- **License**: MIT license

## Pitfalls

- **BAM Index Required**: Input BAM file must be indexed with corresponding .bai file.
- **Reference Genome**: Requires reference FASTA file for visualization.
- **Region Specification**: Must provide genomic region with `-g` or `-a` flag.
- **Memory Usage**: For large BAM files, consider limiting depth with `-d` flag.
- **Vega Dependencies**: For static image output, requires vega-cli and vega-lite-cli packages.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and usage instructions.

### Basic usage with Vega-Lite output
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 > plot.vl.json`
**Explanation:** Generates Vega-Lite JSON specification for alignment plot of specified region.

### Generate interactive HTML report
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 --html > plot.html`
**Explanation:** Creates interactive HTML report with search functionality and read highlighting.

### Specify region by position
**Args:** `alignoth -b sample.bam -r reference.fa -a chr2:17348`
**Explanation:** Visualizes reads around a specific genomic position.

### Highlight specific region
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 -h 210-220`
**Explanation:** Highlights a specific interval within the visualization.

### Set maximum read depth
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 -d 200`
**Explanation:** Limits display to 200 reads to reduce output size.

### Plot all reads in region
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 -p`
**Explanation:** Plots all reads in specified region (use only for small BAM files).

### Generate PDF output
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 | vl2vg | vg2pdf > plot.pdf`
**Explanation:** Pipes Vega-Lite output through vega-cli tools to generate PDF.

### Generate SVG output
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 | vl2vg | vg2svg > plot.svg`
**Explanation:** Pipes Vega-Lite output through vega-cli tools to generate SVG.

### Set maximum plot width
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 -w 1920`
**Explanation:** Sets maximum width of the output plot to 1920 pixels.

### Output to directory
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 -o output_dir/`
**Explanation:** Splits data and Vega-Lite specification into separate files in output directory.

### Interactive wizard mode
**Args:** `alignoth`
**Explanation:** Launches interactive wizard guiding through file selection, region definition, and output format choice.

### Multiple highlight regions
**Args:** `alignoth -b sample.bam -r reference.fa -g chr1:200-300 -h 210 -h 215-218`
**Explanation:** Highlights multiple positions and intervals in the visualization.
