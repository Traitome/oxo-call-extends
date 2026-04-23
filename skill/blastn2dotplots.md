---
name: blastn2dotplots
category: alignment
description: Visualize multiple dot-plot alignments from BLASTN output
tags: [blastn2dotplots, blast, visualization, dotplot, alignment]
author: oxo-call-community
source_url: "https://github.com/mokuno3430/blastn2dotplots"
---

## Concepts

- **Tool Overview**: blastn2dotplots generates dot-plot visualizations from BLASTN output.
- **Core Function**: Creates publication-quality dot plots showing sequence alignments.
- **Input**: BLASTN tabular output (-outfmt 6).
- **Output**: Dot-plot images (PNG/SVG format).
- **Application**: Visualizing genome alignments and synteny.
- **Installation**: Install via bioconda: `conda install -c bioconda blastn2dotplots`

## Pitfalls

- **BLAST Format**: Requires BLASTN tabular output with specific columns.
- **Large Alignments**: Very large alignments may produce large output files.
- **Sequence Names**: Long sequence names may overlap in plots.
- **Memory Usage**: Large number of hits requires significant memory.

## Examples

### Generate dot plot
**Args:** `blastn2dotplots -i blast_results.tsv -o dotplot.png`
**Explanation:** Creates dot-plot visualization from BLASTN output.

### Specify output format
**Args:** `blastn2dotplots -i blast_results.tsv -f svg -o dotplot.svg`
**Explanation:** Outputs dot plot in SVG format for publication.

### Set figure size
**Args:** `blastn2dotplots -i blast_results.tsv -w 10 -h 10 -o dotplot.png`
**Explanation:** Creates 10x10 inch dot plot figure.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
