---
name: scxa-plots
category: visualization
description: scxa-plots - Plotting utilities for Single-cell Expression Atlas analysis
tags: ["scxa-plots", "visualization", "single-cell", "RNA-seq"]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/scxa-plots"
---

## Concepts

- **Tool Overview**: scxa-plots (v0.0.1) provides plotting wrappers for Single-cell Expression Atlas (SCXA) analysis.
- **Core Function**: Generates bespoke plots for single-cell RNA-seq analysis.
- **Algorithm**: Implements various visualization techniques for single-cell data.
- **Input/Output**: Accepts analysis results and produces plot files.
- **SCXA Integration**: Designed for use with EBI's Single-cell Expression Atlas.
- **Applications**: Data visualization, quality control, and result presentation.

## Pitfalls

- **Dependency on SCXA**: Designed for use with SCXA workflow.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Format**: Requires specific input data formats.
- **Documentation**: Some features have limited documentation.
- **Version Compatibility**: Different versions may have breaking changes.
- **Plot Customization**: Limited customization options.

## Examples

### Basic plot generation
**Args:** `scxa-plots generate -i data.h5ad -t umap -o umap.png`
**Explanation:** `-i` input data; `-t` plot type; `-o` output file.

### Quality control plot
**Args:** `scxa-plots qc -i data.h5ad -o qc_report.pdf`
**Explanation:** Generates QC report.

### Expression heatmap
**Args:** `scxa-plots heatmap -i data.h5ad -g gene_list.txt -o heatmap.png`
**Explanation:** `-g` specifies gene list.

### Violin plot
**Args:** `scxa-plots violin -i data.h5ad -g gene_name -o violin.png`
**Explanation:** Generates violin plot for specific gene.

### Verbose logging
**Args:** `scxa-plots generate -i data.h5ad -v -o plot.png`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `scxa-plots --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `scxa-plots --version`
**Explanation:** Shows current version.