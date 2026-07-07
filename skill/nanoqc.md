---
name: nanoqc
category: qc
description: NanoQC - FastQC-like quality control plots for Nanopore sequencing
tags: [nanoqc, qc, nanopore, fastqc, visualization, quality-control]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanoQC"
---

## Concepts

- **Tool Overview**: NanoQC v0.10.0 generates FastQC-like quality control plots specifically optimized for Oxford Nanopore sequencing data.
- **Core Function**: Produces comprehensive quality control reports including read length distribution, quality score histograms, and nucleotide composition plots.
- **Algorithm**: Parses FASTQ files or sequencing summary files to compute quality metrics. Generates interactive HTML reports with matplotlib.
- **Input Format**: Accepts FASTQ (gzipped or uncompressed) and sequencing summary files from Nanopore sequencers.
- **Output**: Produces HTML reports with interactive plots and tabular statistics. Can also output individual plot files.
- **Use Case**: Quality control for Nanopore sequencing runs, batch processing of multiple samples, and generating publication-ready QC reports.

## Pitfalls

- **Memory Usage**: Processing very large FASTQ files may require significant memory. Consider subsampling.
- **File Compression**: Ensure consistent compression when processing multiple files. Mixed compression may cause issues.
- **Sequencing Summary**: Requires properly formatted sequencing summary files from Guppy or Albacore.
- **Plot Customization**: Default plots may need customization for specific use cases.
- **Duplicate Reads**: Does not automatically remove duplicate reads. Consider deduplication before QC.
- **HTML Reports**: Interactive features require a web browser for full functionality.

## Examples

### Basic QC report
**Args:** `-i reads.fastq.gz -o output_dir`
**Explanation:** Generates FastQC-like QC report from Nanopore FASTQ file.

### Use sequencing summary
**Args:** `-s sequencing_summary.txt -o output_dir`
**Explanation:** Generates QC report from sequencing summary file.

### Include both inputs
**Args:** `-i reads.fastq.gz -s sequencing_summary.txt -o output_dir`
**Explanation:** Combines data from both FASTQ and sequencing summary.

### Output individual plots
**Args:** `-i reads.fastq.gz -o output_dir --plots_only`
**Explanation:** Generates only plot files without HTML report.

### Display help
**Args:** `nanoqc --help`
**Explanation:** Shows all available QC options and parameters.
