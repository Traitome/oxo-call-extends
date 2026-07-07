---
name: multiqc_sav
category: qc
description: MultiQC plugin to visualize Illumina Sequencing Analysis Viewer (SAV) plots and run metrics.
tags: [multiqc-sav, multiqc, qc, illumina, sav, sequencing-metrics, quality-control]
author: oxo-call-community
source_url: "https://multiqc.info/"
---

## Concepts

- **Tool Overview**: multiqc_sav v0.2.0 is a MultiQC plugin that parses Illumina Sequencing Analysis Viewer (SAV) output files and generates interactive visualizations of run quality metrics.
- **Core Function**: Extracts quality metrics from Illumina SAV files (Intensities.csv, Control.csv, and runParameters.xml) to display lane-level, tile-level, and cycle-level quality data.
- **Input Format**: Reads Illumina SAV CSV files typically found in the Illumina rtengine output directory. Requires uncompressed SAV files for parsing.
- **Output**: Adds dedicated sections to the MultiQC HTML report with heatmaps showing per-lane and per-tile quality scores, Q-score distributions, and phasing metrics.
- **Installation**: Install via pip (`pip install multiqc_sav`) or Bioconda (`conda install -c bioconda multiqc_sav`). Works with MultiQC >= 1.7.
- **Use Case**: Essential for Illumina sequencer output QC—provides visual overview of run quality across lanes and tiles before downstream analysis.

## Pitfalls

- **Compressed Files**: multiqc_sav cannot read compressed (gzip/zipped) SAV files. Decompress Illumina output before running MultiQC.
- **Missing RunParameters.xml**: The plugin requires runParameters.xml for complete metadata. Without it, some metrics display with incomplete or missing information.
- **Non-Illumina Data**: This module only works with Illumina SAV format. MiSeq, NextSeq, and NovaSeq outputs are supported; other platforms (PacBio, Oxford Nanopore) generate incompatible files.
- **Large Run Files**: High-output Illumina runs (NovaSeq X) produce very large SAV files. Processing may be slow and memory-intensive.
- **Tile Naming Convention**: Different Illumina instruments use different tile naming schemes. multiqc_sav generally handles these, but custom or unusual naming may cause parsing errors.
- **Version Compatibility**: Older multiqc_sav versions may not support newest Illumina output formats. Check for updates when processing recent sequencer outputs.

## Examples

### Generate MultiQC report with SAV data
**Args:** `multiqc illumina_run_directory/ -o qc_reports/`
**Explanation:** Scans the Illumina run directory for SAV files and generates a QC report. The multiqc_sav module activates automatically when installed and SAV files are detected.

### Run only the SAV module
**Args:** `multiqc illumina_run_directory/ --module multiqc_sav -o qc_reports/`
**Explanation:** Forces execution of only the SAV module, skipping all other module searches. Faster for directories containing only Illumina output files.

### Include all subdirectories
**Args:** `multiqc illumina_run_directory/ --fullpath -o qc_reports/`
**Explanation:** Uses `--fullpath` to scan subdirectories with absolute paths. Ensures all nested SAV file locations are found in complex run directory structures.

### Custom sample name cleaning
**Args:** `multiqc illumina_run_directory/ --cl_config "fn_clean_exts: ['_S\d+']" -o qc_reports/`
**Explanation:** Uses MultiQC's command-line config to apply sample name cleaning rules specific to SAV data. Removes lane identifiers for cleaner sample names.

### Export SAV data separately
**Args:** `multiqc illumina_run_directory/ --export -o qc_reports/`
**Explanation:** Exports parsed SAV metrics as JSON files in the multiqc_data/ directory. Useful for loading into external dashboards or creating custom visualizations.

### Combine SAV with FastQC data
**Args:** `multiqc illumina_run_directory/ fastqc_output/ -o combined_qc/`
**Explanation:** Runs both SAV and FastQC modules together to create a comprehensive QC report covering both sequencer run metrics and per-sample sequence quality.
