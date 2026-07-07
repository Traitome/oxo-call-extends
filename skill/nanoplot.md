---
name: nanoplot
category: qc
description: NanoPlot - Plotting suite for long-read sequencing data and alignments
tags: [nanoplot, qc, nanopore, visualization, long-reads, quality-control]
author: oxo-call-community
source_url: "https://github.com/wdecoster/NanoPlot"
---

## Concepts

- **Tool Overview**: NanoPlot v1.46.2 is a comprehensive plotting suite for visualizing long-read sequencing data quality metrics and alignment statistics.
- **Core Function**: Generates publication-quality plots for read length distributions, quality scores, mapping statistics, and other key metrics.
- **Algorithm**: Uses matplotlib and seaborn for visualization. Computes descriptive statistics and generates interactive HTML reports.
- **Input Format**: Accepts FASTQ (gzipped or uncompressed), BAM (aligned reads), and sequencing summary files from Nanopore sequencers.
- **Output**: Produces HTML reports with interactive plots, PNG images, and tabular statistics. Supports multiple plot types.
- **Use Case**: Quality control for Nanopore sequencing runs, comparing sequencing performance, and generating publication-ready figures.

## Pitfalls

- **Memory Usage**: Processing very large files may require significant memory. Consider subsampling for extremely large datasets.
- **BAM Requirements**: BAM files must be sorted and indexed for accurate mapping statistics.
- **Plot Customization**: Default plots may need customization for specific use cases. Check available options.
- **Report Generation**: HTML reports require a web browser for full interactivity. PNG outputs are static.
- **Sequencing Summary**: Requires properly formatted sequencing summary files from Guppy or Albacore.
- **Duplicate Reads**: Does not automatically remove duplicate reads. Consider deduplication before plotting.

## Examples

### Plot from FASTQ
**Args:** `-i reads.fastq.gz -o output_dir`
**Explanation:** Generates QC plots from FASTQ file.

### Plot from BAM
**Args:** `-b aligned.bam -o output_dir`
**Explanation:** Generates QC plots from alignment file including mapping statistics.

### Include sequencing summary
**Args:** `-i reads.fastq.gz -s sequencing_summary.txt -o output_dir`
**Explanation:** Incorporates sequencing summary data for additional metrics.

### Generate only specific plots
**Args:** `-i reads.fastq.gz -o output_dir --plots dot`
**Explanation:** Generates only dot plots (read length vs quality).

### Display help
**Args:** `NanoPlot --help`
**Explanation:** Shows all available plotting options and parameters.
