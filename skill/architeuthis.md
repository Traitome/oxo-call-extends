---
name: architeuthis
category: annotation
description: Tool to analyze and summarize Kraken taxonomic classification data
tags: [architeuthis, annotation, metagenomics, kraken, taxonomic-classification]
author: oxo-call-community
source_url: "https://github.com/cdiener/architeuthis"
---

## Concepts

- **Tool Overview**: Architeuthis is a supplementary tool for analyzing and summarizing data from Kraken taxonomic classifiers (Kraken2, KrakenUniq, Bracken). Version 0.5.0.
- **Core Function**: Provides fast, standalone analysis of taxonomic classification results with enhanced reporting and visualization capabilities.
- **Kraken Integration**: Works with output from Kraken2, KrakenUniq, and Bracken for unified analysis.
- **Metagenomics Analysis**: Designed for metagenomic sample classification and species abundance estimation.
- **Report Generation**: Creates comprehensive reports with taxonomic hierarchies and abundance profiles.
- **Input/Output**: Processes Kraken report files and outputs summaries, visualizations, and statistical analyses.
- **Installation**: `conda install -c bioconda architeuthis` or install via pip.

## Pitfalls

- **Input Format**: Requires Kraken-formatted output. Ensure compatibility with your Kraken version.
- **Database Compatibility**: Results depend on the reference database used for Kraken classification.
- **Large Files**: Large metagenomic datasets may require significant processing time and memory.
- **Threshold Settings**: Classification thresholds affect sensitivity and specificity of results.
- **Novel Organisms**: Novel species not in database will be classified at higher taxonomic levels.

## Examples

### Display help
**Args:** `architeuthis --help`
**Explanation:** Shows all available command-line options and usage information.

### Generate summary report
**Args:** `architeuthis summarize --input kraken_report.txt --output summary.csv`
**Explanation:** Generates CSV summary of taxonomic classification with abundance information.

### Visualize taxonomy
**Args:** `architeuthis plot --input kraken_report.txt --output tax_profile.pdf --top 20`
**Explanation:** Creates PDF visualization of top 20 most abundant taxa.

### Compare samples
**Args:** `architeuthis compare --inputs sample1.txt sample2.txt --output comparison.csv`
**Explanation:** Compares taxonomic profiles between multiple samples.

### Filter by abundance
**Args:** `architeuthis filter --input report.txt --threshold 0.01 --output filtered.txt`
**Explanation:** Filters taxa to those with relative abundance above 1%.

### Export for downstream analysis
**Args:** `architeuthis export --input kraken.txt --format biom --output tax.biom`
**Explanation:** Exports classification results in BIOM format for QIIME2 or other tools.

### Generate interactive report
**Args:** `architeuthis report --input sample.kraken --outdir html_report/`
**Explanation:** Creates interactive HTML report with clickable taxonomy browser.