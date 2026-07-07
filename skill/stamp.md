---
name: stamp
category: metagenomics
description: A software package for analyzing taxonomic and functional profiles.
tags: [stamp, metagenomics, statistical-analysis, visualization]
author: oxo-call-community
source_url: "http://pypi.python.org/pypi/stamp/"
---

## Concepts

- **Tool Overview**: stamp (v2.1.3) is a software package for analyzing and visualizing taxonomic and functional profiles from metagenomic data.
- **Core Function**: Performs statistical comparison of microbial communities across samples and groups.
- **Statistical Methods**: Supports various statistical tests including ANOVA, Kruskal-Wallis, and Fisher's exact test.
- **Input/Output**: Input: OTU tables or taxonomic profiles; Output: Statistical reports and visualizations.
- **Visualization**: Generates bar charts, heatmaps, and rarefaction curves for data exploration.
- **Installation**: `conda install -c bioconda stamp` or `pip install stamp`.

## Pitfalls

- **Data Format**: Requires specific input format; incorrect formatting causes analysis failures.
- **Sample Size**: Small sample sizes may produce unreliable statistical results.
- **Multiple Testing**: Requires appropriate correction for multiple hypothesis testing.
- **Normalization**: Improper data normalization affects statistical comparisons.
- **Memory Usage**: Large datasets may require significant memory for analysis.
- **Visualization Limits**: Very large datasets may produce cluttered visualizations.

## Examples

### Display help
**Args:** `stamp --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `stamp -i otu_table.txt -o results/`
**Explanation:** Run basic analysis on OTU table.

### Statistical testing
**Args:** `stamp -i otu_table.txt -o results/ --test kruskal`
**Explanation:** Perform Kruskal-Wallis test for group comparisons.

### Generate heatmap
**Args:** `stamp -i otu_table.txt -o heatmap.png --heatmap`
**Explanation:** Generate heatmap visualization of taxonomic profiles.

### Rarefaction analysis
**Args:** `stamp -i otu_table.txt -o rarefaction.png --rarefaction`
**Explanation:** Generate rarefaction curves for alpha diversity.

### Multiple groups
**Args:** `stamp -i otu_table.txt -o results/ -g groups.txt`
**Explanation:** Analyze data with predefined group assignments.

### Filter low-abundance taxa
**Args:** `stamp -i otu_table.txt -o results/ --min-abundance 0.01`
**Explanation:** Filter taxa with abundance below 1%.

### Verbose mode
**Args:** `stamp -i otu_table.txt -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output format
**Args:** `stamp -i otu_table.txt -o results/ --format pdf`
**Explanation:** Output visualizations in PDF format.
