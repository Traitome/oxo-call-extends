---
name: checkqc
category: qc
description: Parse Illumina NGS data and check it for quality criteria
tags: [checkqc, ngs, quality-control, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://checkqc.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: CheckQC is a program for parsing Illumina NGS data and checking it against user-defined quality criteria.
- **Core Function**: Validates sequencing data quality metrics against configurable thresholds and generates reports.
- **Features**: Fastq quality checking, adapter content detection, sequence duplication, and quality threshold validation.
- **Input**: Illumina Fastq files (single-end or paired-end) and optional sample sheet.
- **Output**: Quality reports with pass/fail status for each QC criterion.
- **Application**: Pre-sequencing quality control for Illumina sequencing runs.
- **Installation**: Install via bioconda: `conda install -c bioconda checkqc`

## Pitfalls

- **Illumina Specific**: Designed specifically for Illumina sequencing data.
- **Fastq Format**: Requires properly formatted Fastq files.
- **Quality Thresholds**: Default thresholds may not suit all experiments.
- **Sample Sheet**: Sample sheet format must match Illumina standards.
- **Adapter Detection**: May miss non-standard adapters.

## Examples

### Run QC on Fastq files
**Args:** `checkqc -i sample_R1.fastq.gz sample_R2.fastq.gz -o report.html`
**Explanation:** Performs QC analysis on paired-end Fastq files.

### With sample sheet
**Args:** `checkqc -i sample_R1.fastq.gz -s SampleSheet.csv -o report.html`
**Explanation:** Uses sample sheet for additional metadata validation.

### Custom thresholds
**Args:** `checkqc -i reads.fastq -c custom_config.yaml -o report.html`
**Explanation:** Uses custom QC thresholds from configuration file.

### Display help
**Args:** `checkqc --help`
**Explanation:** Shows all available options and usage information.