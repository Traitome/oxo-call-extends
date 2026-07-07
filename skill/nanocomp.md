---
name: nanocomp
category: qc
description: NanoComp - Compare Oxford Nanopore sequencing runs and alignments
tags: [nanocomp, qc, nanopore, comparison, visualization, statistics]
author: oxo-call-community
source_url: "https://github.com/wdecoster/NanoComp"
---

## Concepts

- **Tool Overview**: NanoComp v1.25.6 is a tool for comparing multiple Oxford Nanopore sequencing runs and alignments. It generates comprehensive statistics and visualizations for quality control and comparison.
- **Core Function**: Compares read length distributions, quality scores, mapping statistics, and other metrics across multiple sequencing runs or samples.
- **Algorithm**: Parses sequencing data and alignment files, computes descriptive statistics, and generates comparative visualizations using matplotlib and seaborn.
- **Input Format**: Accepts FASTQ, BAM, and sequencing summary files from Nanopore runs. Supports multiple samples for comparison.
- **Output**: Produces HTML reports with interactive plots, PDF reports, and tabular statistics comparing the input datasets.
- **Use Case**: Quality control for Nanopore sequencing, comparing sequencing runs, monitoring sequencing performance over time, and identifying batch effects.

## Pitfalls

- **Memory Usage**: Processing very large FASTQ/BAM files requires sufficient memory. Consider subsampling for extremely large datasets.
- **File Compression**: Ensure input files are properly compressed/uncompressed as expected. Mixed compression may cause parsing errors.
- **Alignment Format**: BAM files must be properly sorted and indexed for accurate mapping statistics.
- **Sample Names**: Provide meaningful sample names for clear comparison in plots. Default names may be confusing.
- **Report Generation**: HTML reports require a web browser for full interactivity. PDF reports are static.
- **Nanopore Specific**: Designed specifically for Nanopore data. May produce unexpected results with other sequencing technologies.

## Examples

### Compare FASTQ files
**Args:** `-f run1.fastq run2.fastq -n Run1 Run2 -o output_dir`
**Explanation:** Compares multiple Nanopore runs based on raw FASTQ data.

### Compare alignment files
**Args:** `-b aligned1.bam aligned2.bam -n Sample1 Sample2 -o output_dir`
**Explanation:** Compares alignment statistics across multiple BAM files.

### Include sequencing summary
**Args:** `-f reads.fastq -s sequencing_summary.txt -o report/`
**Explanation:** Incorporates sequencing summary data for additional metrics.

### Generate PDF report
**Args:** `-f run*.fastq -n Run1 Run2 Run3 -o report/ --pdf`
**Explanation:** Generates PDF report alongside HTML output.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameter descriptions.
