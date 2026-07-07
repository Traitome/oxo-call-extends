---
name: stacks_summary
category: utility
description: Stacks reports generator for summarizing population genomics results.
tags: [stacks_summary, reporting, population-genomics]
author: oxo-call-community
source_url: "https://github.com/mariabernard/galaxy_wrappers"
---

## Concepts

- **Tool Overview**: stacks_summary is a utility for generating summary reports from Stacks population genomics pipeline output.
- **Core Function**: Compiles and visualizes results from Stacks analyses including SNP statistics and population structure.
- **Report Components**: Summary statistics, SNP distributions, population differentiation metrics, and visualizations.
- **Input/Output**: Input: Stacks populations output files; Output: HTML report with tables and plots.
- **Visualization**: Generates bar charts, histograms, and heatmaps for population genetics data.
- **Installation**: `conda install -c bioconda stacks_summary` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific file structure from Stacks populations output.
- **Missing Files**: Incomplete input files cause report generation failures.
- **Large Datasets**: May require significant memory for large population datasets.
- **Visualization Limits**: Very large datasets may produce cluttered visualizations.
- **Version Compatibility**: Output format changes between Stacks versions may affect compatibility.
- **Customization**: Limited customization options for report layout and content.

## Examples

### Display help
**Args:** `stacks_summary --help`
**Explanation:** Shows available options and usage information.

### Basic report generation
**Args:** `stacks_summary -i stacks_output/ -o report.html`
**Explanation:** Generate summary report from Stacks output directory.

### With population map
**Args:** `stacks_summary -i stacks_output/ -o report.html -m populations_map.txt`
**Explanation:** Include population map information in report.

### SNP statistics only
**Args:** `stacks_summary -i stacks_output/ -o snp_stats.txt --stats-only`
**Explanation:** Output only SNP statistics without visualizations.

### Custom title
**Args:** `stacks_summary -i stacks_output/ -o report.html -t "My Population Analysis"`
**Explanation:** Set custom report title.

### Include PCA
**Args:** `stacks_summary -i stacks_output/ -o report.html --pca`
**Explanation:** Include PCA analysis in report.

### Quality filtering
**Args:** `stacks_summary -i stacks_output/ -o report.html -q 30`
**Explanation:** Filter SNPs by minimum quality score.

### Verbose mode
**Args:** `stacks_summary -i stacks_output/ -o report.html -v`
**Explanation:** Run with detailed logging for debugging.
