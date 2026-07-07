---
name: ig-flowtools
category: utility
description: Set of tools for flow cytometry analysis, part of the ImmPort ecosystem
tags: [ig-flowtools, flow cytometry, immunology, ImmPort]
author: oxo-call-community
source_url: "https://github.com/ImmPortDB/ig-flowtools"
---

## Concepts

- **Tool Overview**: ig-flowtools is a comprehensive suite of tools for flow cytometry data analysis within the ImmPort ecosystem
- **Core Function**: Provides tools for quality control, visualization, and analysis of flow cytometry experiments
- **Input/Output**: Supports FCS format files; generates analysis reports and visualizations
- **Installation**: `conda install -c bioconda ig-flowtools`
- **Dependencies**: Includes flowAI, flowCore, flowViz, and ggcyto for advanced flow cytometry analysis

## Pitfalls

- **Data Standardization**: Requires consistent gating strategies across experiments for meaningful comparisons
- **Compensation Controls**: Incorrect compensation can distort population identification
- **File Format Compatibility**: Older FCS file formats may not be fully supported
- **Memory Requirements**: Large flow cytometry datasets can require substantial memory for analysis
- **Software Dependencies**: Relies on multiple R/Bioconductor packages that may have version conflicts

## Examples

### Run quality control on FCS files
**Args:** `ig-flowtools quality -i fcs_files/ -o qc_report.pdf`
**Explanation:** Performs quality control checks on flow cytometry data and generates a comprehensive report.

### Perform automated gating
**Args:** `ig-flowtools gate -i sample.fcs -g gating_strategy.xml -o gated_results/`
**Explanation:** Applies a predefined gating strategy to identify cell populations.

### Generate flow cytometry plots
**Args:** `ig-flowtools plot -i sample.fcs -o plots/ --type density`
**Explanation:** Creates density plots and other visualizations from flow cytometry data.

### Analyze multiple samples
**Args:** `ig-flowtools analyze -i samples/ -o analysis_results/ --panel markers.csv`
**Explanation:** Batch processes multiple FCS files with a defined marker panel.

### Export results to ImmPort format
**Args:** `ig-flowtools export -i results/ -o immport_export/ --format immport`
**Explanation:** Converts analysis results to ImmPort-compatible format for data submission.
