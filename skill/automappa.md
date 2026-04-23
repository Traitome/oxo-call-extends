---
name: automappa
category: metagenomics
description: Automappa - Interactive interface for exploration and refinement of metagenome-assembled genomes
tags: [metagenomics, binning, visualization, genome-refinement, interactive]
author: oxo-call-community
source_url: "https://github.com/WiscEvan/Automappa"
---

## Concepts

- **Tool Overview**: Automappa is an interactive interface for exploring and refining metagenome-assembled genomes (MAGs) from Autometa taxonomic classification and binning results.

- **Autometa Integration**: Designed as companion tool to Autometa, providing visual interface for examining and refining binning results.

- **Interactive Refinement**: Allows manual adjustment of taxonomic assignments and genome bin boundaries through intuitive web interface.

- **Quality Assessment**: Visualizes completeness, contamination, and other quality metrics for genome bins.

- **Taxonomic Exploration**: Enables exploration of taxonomic composition and distribution across metagenome samples.

## Pitfalls

- **Autometa Dependency**: Requires Autometa output files. Cannot be used with other binning tools' results.

- **Manual Curation Bias**: User decisions during manual refinement can introduce bias. Document all modifications.

- **Web Interface**: Runs as web application, requiring browser and potentially server setup for remote access.

- **Large Datasets**: Very large metagenomes may have slow interface response times.

## Examples

### Launch interactive interface
**Args:** `automappa run --input autometa_results.tsv --output refined_bins/`
**Explanation:** Starts Automappa web interface for exploring Autometa results, saves refined bins to output directory.

### Specify port for web server
**Args:** `automappa run --input autometa_results.tsv --port 8050`
**Explanation:** Runs web interface on custom port 8050 instead of default, useful when default port is occupied.

### Export refined bins
**Args:** `automappa export --input autometa_results.tsv --refinements manual_edits.json --output final_bins/`
**Explanation:** Exports genome bins after applying manual refinements saved in JSON file.

### Quality summary report
**Args:** `automappa report --input autometa_results.tsv --output quality_report.html`
**Explanation:** Generates static HTML report of genome bin quality metrics without launching interactive interface.

### Batch binning visualization
**Args:** `automappa batch --input-dir autometa_outputs/ --output-dir reports/`
**Explanation:** Processes multiple Autometa result files, generating quality reports for each.
