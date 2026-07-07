---
name: sashimi-py
category: visualization
description: Pure Python implementation of sashimi plots for RNA-seq data visualization
tags: ["sashimi-py", "visualization", "RNA-seq", "alternative-splicing"]
author: oxo-call-community
source_url: "https://sashimi.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: sashimi-py (v0.1.5) is a pure Python implementation of sashimi plots for visualizing RNA-seq read alignments and alternative splicing patterns.
- **Core Function**: Generates publication-quality visualizations of splice junctions and read densities across genomic regions.
- **Algorithm**: Plots RNA-seq read densities along exons and junctions, with arc heights proportional to junction read counts.
- **Input Formats**: Supports BAM, BED, bigWig, GTF, and other standard bioinformatics formats.
- **Output**: Produces publication-quality figures in multiple formats (PDF, PNG, SVG).
- **Applications**: Visualizing alternative splicing events, isoform expression patterns, and transcript structure.

## Pitfalls

- **Memory Usage**: Processing large BAM files requires substantial memory.
- **Computational Time**: Generating plots for large genomic regions can be slow.
- **Alignment Quality**: Results depend on properly aligned reads with junction information.
- **Visual Complexity**: Overlapping transcripts can create cluttered visualizations.
- **Parameter Sensitivity**: Arc height scaling and color schemes require careful tuning.
- **Browser Integration**: Limited interactive capabilities compared to genome browsers.

## Examples

### Basic sashimi plot
**Args:** `sashimi --bam sample1.bam --gtf genes.gtf --region chr1:100000-105000 -o plot.pdf`
**Explanation:** Generates sashimi plot for specified genomic region from BAM and GTF files.

### Multiple samples
**Args:** `sashimi --bam sample1.bam sample2.bam --gtf genes.gtf --region chr1:100000-105000 -o multi_sample.pdf`
**Explanation:** Plots multiple samples together for comparison.

### Custom colors
**Args:** `sashimi --bam sample.bam --gtf genes.gtf --region chr1:100000-105000 --colors red,blue -o plot.pdf`
**Explanation:** Specifies custom colors for different samples.

### Include junction labels
**Args:** `sashimi --bam sample.bam --gtf genes.gtf --region chr1:100000-105000 --label-junctions -o plot.pdf`
**Explanation:** Adds junction read count labels to arcs.

### Adjust arc height
**Args:** `sashimi --bam sample.bam --gtf genes.gtf --region chr1:100000-105000 --max-arc-height 50 -o plot.pdf`
**Explanation:** Sets maximum arc height to 50 for better visualization.

### Output as SVG
**Args:** `sashimi --bam sample.bam --gtf genes.gtf --region chr1:100000-105000 -o plot.svg`
**Explanation:** Outputs plot in SVG format for vector graphics editing.

### With gene expression values
**Args:** `sashimi --bam sample.bam --gtf genes.gtf --expr expression.tsv --region chr1:100000-105000 -o plot.pdf`
**Explanation:** Integrates gene expression values into the visualization.