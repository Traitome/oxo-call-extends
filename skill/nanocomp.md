---
name: nanocomp
category: qc
description: Comparing runs of Oxford Nanopore sequencing data and alignments
tags: [nanocomp, qc, nanopore, comparison, visualization]
author: oxo-call-community
source_url: "https://github.com/wdecoster/NanoComp"
---

## Concepts

- **Tool Overview**: NanoComp v1.25.6 - compares Oxford Nanopore sequencing runs and alignments.
- **Core Function**: Generates comparative statistics and visualizations for multiple Nanopore runs.
- **Input/Output**: Takes FASTQ/BAM files from multiple runs; outputs comparative plots and statistics.
- **Installation**: `conda install -c bioconda nanocomp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports FASTQ and BAM formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Compare runs
**Args:** `-f run1.fastq run2.fastq -n Run1 Run2 -o output_dir`
**Explanation:** Compares multiple Nanopore runs with comparative plots.

### Compare alignments
**Args:** `-b aligned1.bam aligned2.bam -n Sample1 Sample2 -o output_dir`
**Explanation:** Compares multiple alignment files.
