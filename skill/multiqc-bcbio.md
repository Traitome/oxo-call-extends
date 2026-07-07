---
name: multiqc-bcbio
category: qc
description: MultiQC plugin for bcbio report visualization and quality control aggregation.
tags: [multiqc-bcbio, multiqc, qc, bcbio, visualization, quality-control]
author: oxo-call-community
source_url: "https://multiqc.info/docs/modules/bcbio/"
---

## Concepts

- **Tool Overview**: multiqc-bcbio v0.2.9 is a MultiQC plugin that parses and visualizes output from the bcbio-nextgen pipeline. It integrates seamlessly with MultiQC to combine bcbio metrics with other NGS QC data.
- **Core Function**: Extracts quality metrics, alignment statistics, and variant calling summaries from bcbio output files and presents them in MultiQC's aggregated HTML report format.
- **Input Format**: Reads bcbio-generated JSON summary files and CSV metrics files from the bcbio project structure (project/final, project/qc).
- **Output**: Adds dedicated sections to the MultiQC HTML report with tables and plots for alignment metrics, sequencing quality, and variant statistics.
- **Installation**: Available via pip (`pip install multiqc-bcbio`) and Bioconda (`conda install -c bioconda multiqc-bcbio`). Requires MultiQC >= 1.2 as a dependency.
- **Integration**: Automatically loaded when MultiQC runs if installed. No explicit module selection needed—MultiQC auto-discovers bcbio output files.

## Pitfalls

- **Missing Summary Files**: MultiQC cannot find bcbio output if the project directory structure is modified. Ensure standard bcbio layout with config/, final/, and qc/ subdirectories.
- **Version Mismatch**: Older bcbio versions may output metrics in formats incompatible with newer multiqc-bcbio. Check version compatibility before upgrading.
- **Mixed Case Sample Names**: bcbio sometimes produces sample names with mixed case or special characters. MultiQC may fail to properly aggregate data across samples.
- **Incomplete Runs**: If bcbio run terminated early, missing metrics cause sections to display with empty data or error messages in the MultiQC report.
- **Memory Usage**: Large bcbio projects with many samples generate large JSON files. MultiQC may run slowly or exhaust memory when processing extensive datasets.
- **Bioconda Channel Order**: When installing via conda, ensure correct channel order (bioconda, conda-forge) to avoid dependency conflicts with multiqc.

## Examples

### Generate MultiQC report with bcbio data
**Args:** `multiqc project_directory/ -o qc_reports/`
**Explanation:** Scans the bcbio project directory recursively, finds bcbio output files, and generates an aggregated QC report in qc_reports/. The bcbio plugin modules load automatically if multiqc-bcbio is installed.

### Force overwrite existing report
**Args:** `multiqc project_directory/ -o qc_reports/ -f`
**Explanation:** Uses `-f` (force) to overwrite any existing MultiQC report in the output directory. Useful when re-running after updated bcbio analysis.

### Specify custom config file
**Args:** `multiqc project_directory/ -c custom_config.yaml -o qc_reports/`
**Explanation:** Applies custom MultiQC configuration settings (fn_clean_exts, module_order, etc.) while processing bcbio data. Config file follows MultiQC YAML format.

### Include only bcbio modules
**Args:** `multiqc project_directory/ --module bcbio -o qc_reports/`
**Explanation:** Runs only the bcbio module instead of all discovered modules. Faster for projects where only bcbio metrics are needed.

### Ignore specific directories
**Args:** `multiqc project_directory/ --ignore 'work/' --ignore 'upload/' -o qc_reports/`
**Explanation:** Excludes bcbio work directories and upload directories from the scan. Reduces clutter in the report and speeds up processing.

### Export report data as JSON
**Args:** `multiqc project_directory/ --export`
**Explanation:** Exports all parsed data as JSON files in multiqc_data/ directory alongside the HTML report. Allows downstream processing of bcbio metrics in custom scripts.
