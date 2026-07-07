---
name: dnadotplot
category: utility
description: dnadotplot - DNA dot plot visualization tool.
tags: [dnadotplot, utility, visualization, dot-plot, alignment, comparison]
author: oxo-call-community
source_url: "https://github.com/biopython/dnadotplot"
---

## Concepts

- **Tool Overview**: dnadotplot is a tool for generating dot plots of DNA sequence comparisons.
- **Core Function**: Creates visual dot plots comparing DNA sequences to identify similarities.
- **Input/Output**: Input: FASTA sequences. Output: Dot plot images (PNG/SVG).
- **Algorithm**: Compares sequences and plots matches as dots in matrix.
- **Key Features**: Sequence comparison, similarity visualization, customizable output, multiple formats, self-comparison support.
- **Installation**: `conda install -c bioconda dnadotplot`

## Pitfalls

- **Input Requirements**: Requires DNA sequences in FASTA format.
- **Sequence Length**: Very long sequences produce large output files.
- **Memory Usage**: May require significant memory for large comparisons.
- **Visualization Quality**: Too many matches can obscure patterns.
- **Output Size**: High-resolution plots may be large.

## Examples

### Generate dot plot
**Args:** `dnadotplot --seq1 seq1.fa --seq2 seq2.fa --output dotplot.png`
**Explanation:** Generates dot plot comparing two DNA sequences.

### Self-comparison
**Args:** `dnadotplot --seq1 sequence.fa --seq2 sequence.fa --output self_plot.png`
**Explanation:** Compare sequence against itself to find repeats.

### Custom resolution
**Args:** `dnadotplot --seq1 seq1.fa --seq2 seq2.fa --output dotplot.png --dpi 300`
**Explanation:** Generate high-resolution dot plot.

### SVG output
**Args:** `dnadotplot --seq1 seq1.fa --seq2 seq2.fa --output dotplot.svg`
**Explanation:** Generate vector format dot plot.

### Threshold filtering
**Args:** `dnadotplot --seq1 seq1.fa --seq2 seq2.fa --output dotplot.png --threshold 0.8`
**Explanation:** Filter matches by similarity threshold.