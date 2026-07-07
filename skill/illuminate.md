---
name: illuminate
category: programming
description: Analytics toolkit for Illumina sequencer metrics.
tags: [illuminate, programming, metrics, illumina]
author: oxo-call-community
source_url: "https://bitbucket.org/invitae/illuminate"
---

## Concepts

- **Tool Overview**: illuminate (v0.6.3) - A Python analytics toolkit for parsing and analyzing Illumina sequencer metrics and run data
- **Core Function**: Parses RunInfo.xml, SampleSheet.csv, and other Illumina run metadata for quality control and reporting
- **Input/Output**: Reads Illumina run metadata files, outputs structured data for further analysis
- **Installation**: `conda install -c bioconda illuminate` or `pip install illuminate`
- **Key Features**: Supports barcode demultiplexing statistics, lane-level metrics, and run quality assessment

## Pitfalls

- **Version Differences**: API changes between versions may break existing scripts
- **Sample Sheet Format**: Strict format requirements; malformed CSV files cause parsing errors
- **Run Folder Structure**: Requires standard Illumina run folder organization
- **Barcode Complexity**: Handling dual-indexed samples requires careful configuration
- **Data Volume**: Large sequencing runs may require memory optimization

## Examples

### Parse run information
**Args:** `illuminate parse-run --run-folder /path/to/run --output run_info.json`
**Explanation:** Parses RunInfo.xml and generates JSON output with run parameters.

### Extract sample metrics
**Args:** `illuminate sample-metrics --sample-sheet SampleSheet.csv --output metrics.csv`
**Explanation:** Extracts per-sample metrics from SampleSheet and generates CSV report.

### Validate sample sheet
**Args:** `illuminate validate-sheet SampleSheet.csv`
**Explanation:** Validates SampleSheet.csv format and reports any errors or warnings.

### Generate quality report
**Args:** `illuminate quality-report --run-folder /path/to/run --output report.html`
**Explanation:** Generates HTML quality report with run statistics and visualizations.

### Analyze barcode distribution
**Args:** `illuminate barcode-stats --fastq-dir fastq/ --output barcode_counts.csv`
**Explanation:** Analyzes barcode distribution across sequenced samples.

### Merge multiple run reports
**Args:** `illuminate merge-reports --reports report1.json report2.json --output combined.json`
**Explanation:** Merges quality reports from multiple sequencing runs into single output.