---
name: nanoplot
category: qc
description: Plotting suite for long read sequencing data and alignments.
tags: [nanoplot, qc, nanopore, visualization, long-reads]
author: oxo-call-community
source_url: "https://github.com/wdecoster/NanoPlot"
---

## Concepts

- **Tool Overview**: NanoPlot v1.46.2 - plotting suite for long read sequencing data and alignments.
- **Core Function**: Generates quality control plots for Nanopore and other long-read data including read length, quality, and alignment statistics.
- **Input/Output**: Takes FASTQ, BAM, or sequencing_summary.txt; outputs HTML/PNG plots and statistics.
- **Installation**: `conda install -c bioconda nanoplot`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports FASTQ, BAM, and sequencing summary formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Plot from FASTQ
**Args:** `-i reads.fastq.gz -o output_dir`
**Explanation:** Generates QC plots from FASTQ file.

### Plot from BAM
**Args:** `-b aligned.bam -o output_dir`
**Explanation:** Generates QC plots from alignment file.
