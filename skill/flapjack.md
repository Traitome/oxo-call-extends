---
name: flapjack
category: variant-calling
description: "Flapjack is a Java-based application for interactive visualization and analysis of high-throughput genotyping data from SNP arrays and sequencing."
tags: [flapjack, variant-calling, visualization, genotyping, bioinformatics, genetics, population]
author: oxo-call-community
source_url: "https://ics.hutton.ac.uk/flapjack"
---

## Concepts
- **Tool Overview**: Flapjack is a desktop application for visualizing and analyzing large-scale genotyping data. It provides interactive heatmaps, phylogenetic trees, and genotype comparisons.
- **Core Function**: Visualizes genotype data to identify patterns, outliers, and relationships between individuals or populations. Supports SNP array and sequencing-based genotyping data.
- **Input/Output**: Input: Genotype files in various formats (ABH, HapMap, VCF, IMPUTE). Output: Interactive visualizations, exported images, genotype statistics.
- **Visualization Modes**: Heatmap view for genotype patterns, chromosome view for positional data, tree view for population relationships.
- **Data Filtering**: Supports filtering by quality scores, allele frequency, missing data percentage, and custom criteria.
- **Population Analysis**: Enables comparison of genotype frequencies across populations and identification of population-specific markers.
- **Installation**: `conda install -c bioconda flapjack` or download from official website. Requires Java 8+.

## Pitfalls
- **Java Version Compatibility**: Requires Java 8 or later. Older Java versions cause compatibility issues.
- **Memory Requirements**: Large datasets require increased heap size. Configure Java heap settings for optimal performance.
- **File Format Limitations**: Some VCF features may not be fully supported. Convert to ABH format for best results.
- **Missing Data Handling**: High levels of missing data can distort visualizations. Filter or impute before analysis.
- **Performance Issues**: Very large datasets (>100K markers) may have slow rendering. Consider subsetting data.
- **Platform Specificity**: Desktop application only. No command-line interface for batch processing.

## Examples
### Launch Flapjack GUI
**Args:** `flapjack`
**Explanation:** Launches the Flapjack graphical user interface for interactive visualization.

### Load genotype data from file
**Args:** `flapjack -f genotypes.abh -c chromosomes.txt -m markers.txt`
**Explanation:** Loads ABH format genotype file with chromosome and marker information.

### Open VCF file
**Args:** `flapjack -vcf variants.vcf -ref reference.fasta`
**Explanation:** Opens VCF file for visualization with reference genome integration.

### Export visualization as image
**Args:** `flapjack -f genotypes.abh -export-png output.png -width 1920 -height 1080`
**Explanation:** Exports genotype heatmap visualization as high-resolution PNG image.

### Run batch analysis script
**Args:** `flapjack -script analysis.flapjack`
**Explanation:** Executes a Flapjack script file for automated analysis workflows.
