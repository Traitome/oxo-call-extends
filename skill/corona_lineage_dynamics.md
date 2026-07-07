---
name: corona_lineage_dynamics
category: utility
description: Analyzing and visualizing pangolin lineages of GISAID metadata
tags: [corona_lineage_dynamics, sars-cov-2, lineage-analysis, gisaid, visualization]
author: oxo-call-community
source_url: "https://github.com/hzi-bifo/corona_lineage_dynamics"
---

## Concepts

- **Tool Overview**: Corona Lineage Dynamics is a tool for analyzing and visualizing pangolin lineages from GISAID metadata, specifically designed for SARS-CoV-2 variant tracking.
- **Core Function**: Processes GISAID metadata to analyze lineage distribution, temporal dynamics, and geographic spread of SARS-CoV-2 variants.
- **Algorithm**: Parses pangolin lineage assignments and generates statistical summaries and visualizations.
- **Input**: GISAID metadata files, pangolin lineage assignments.
- **Output**: Lineage distribution reports, temporal trend plots, geographic heatmaps.
- **Application**: COVID-19 surveillance, variant tracking, epidemiological analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda corona_lineage_dynamics`

## Pitfalls

- **Data Quality**: Results depend on complete and accurate metadata.
- **Lineage Updates**: Pangolin lineages are regularly updated; use latest version.
- **Geographic Data**: Incomplete location data may affect spatial analysis.
- **File Format**: Requires specific GISAID metadata format.
- **Large Datasets**: May require significant memory for large metadata files.

## Examples

### Analyze lineage distribution
**Args:** `corona_lineage_dynamics -i metadata.tsv -o lineage_analysis/`
**Explanation:** Analyzes lineage distribution from GISAID metadata.

### Generate temporal trends
**Args:** `corona_lineage_dynamics -i metadata.tsv --temporal -o trends.png`
**Explanation:** Generates temporal trend plot of lineage frequencies.

### Geographic visualization
**Args:** `corona_lineage_dynamics -i metadata.tsv --geographic -o map.png`
**Explanation:** Creates geographic heatmap of lineage distribution.

### Filter by date range
**Args:** `corona_lineage_dynamics -i metadata.tsv --start-date 2023-01-01 --end-date 2023-12-31 -o year_analysis/`
**Explanation:** Analyzes lineage dynamics within specific date range.

### Display help
**Args:** `corona_lineage_dynamics --help`
**Explanation:** Shows all available options and usage information.