---
name: fadapa
category: qc
description: "FAstqc DAta PArser - A minimal parser to parse FastQC output data"
tags: [fadapa, qc, FastQC, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fadapa/fadapa"
---

## Concepts

- **Tool Overview**: fadapa is a minimal parser for FastQC output data, designed to extract and analyze quality control metrics from sequencing data.
- **Core Function**: Parses FastQC HTML reports and extracts quality control statistics for downstream analysis.
- **Input/Output**: Input: FastQC HTML report. Output: Parsed quality metrics (JSON/CSV), summary statistics.
- **Algorithm**: Parses HTML structure to extract quality control metrics including per-base quality, sequence content, and adapter content.
- **Key Features**: FastQC report parsing, quality metric extraction, summary generation, batch processing, integration with pipelines.
- **Installation**: `conda install -c bioconda fadapa`

## Pitfalls

- **Report Format**: Requires standard FastQC HTML format.
- **Version Compatibility**: May not support all FastQC versions.
- **Report Integrity**: Corrupted reports may cause parsing errors.
- **Memory Usage**: Large reports may require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic parsing
**Args:** `fadapa -i fastqc_report.html -o quality_metrics.json`
**Explanation:** Parses FastQC report and outputs quality metrics.

### Extract specific modules
**Args:** `fadapa -i fastqc_report.html -o quality_metrics.json --modules "Per base sequence quality,Per sequence quality scores"`
**Explanation:** Extracts specific QC modules from report.

### CSV output
**Args:** `fadapa -i fastqc_report.html -o quality_metrics.csv --csv`
**Explanation:** Outputs quality metrics in CSV format.

### Batch processing
**Args:** `fadapa -i fastqc_reports/ -o results/ --batch`
**Explanation:** Processes multiple FastQC reports in batch mode.

### Summary statistics
**Args:** `fadapa -i fastqc_report.html -o summary.txt --summary`
**Explanation:** Generates summary statistics from QC report.