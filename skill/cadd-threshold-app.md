---
name: cadd-threshold-app
category: visualization
description: Shiny-for-Python app for exploring ClinVar distributions across CADD score thresholds
tags: [cadd, threshold, clinvar, visualization, shiny]
author: oxo-call-community
source_url: "https://github.com/kircherlab/CADD_threshold_app"
---

## Concepts

- **Tool Overview**: cadd-threshold-app is a Shiny-for-Python application for exploring ClinVar distributions across CADD score thresholds.
- **Core Function**: Interactive visualization of ClinVar variant classifications at different CADD score cutoffs.
- **Input**: CADD scores and ClinVar annotations.
- **Output**: Interactive web interface showing variant distributions.
- **Application**: Evaluating optimal CADD thresholds for variant filtering.
- **Installation**: Install via bioconda: `conda install -c bioconda cadd-threshold-app`

## Pitfalls

- **Web Application**: Runs as local web server; not a command-line tool.
- **Data Required**: Requires pre-computed CADD scores with ClinVar annotations.
- **Python Dependency**: Requires Python and Shiny runtime.
- **Interactive Use**: Designed for interactive exploration, not batch processing.

## Examples

### Launch app
**Args:** `cadd-threshold-app`
**Explanation:** Launches the interactive Shiny application in browser.

### Specify data file
**Args:** `cadd-threshold-app --data clinvar_cadd.tsv`
**Explanation:** Launches app with specified data file.

### Set port
**Args:** `cadd-threshold-app --port 8080`
**Explanation:** Launches app on custom port.