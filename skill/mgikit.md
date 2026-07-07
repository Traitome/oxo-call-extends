---
name: mgikit
category: qc
description: mgikit is a collection of tools used to demultiplex fastq files and generate demultiplexing and quality reports.
tags: [mgikit, qc, sequence]
author: oxo-call-community
source_url: "https://sagc-bioinformatics.github.io/mgikit"
---

## Concepts

- **Tool Overview**: mgikit v2.1.1 is a collection of tools for demultiplexing FASTQ files and generating quality reports.
- **Core Function**: Demultiplexes sequencing data and generates quality control reports.
- **Demultiplexing**: Separates multiplexed sequencing reads by barcodes.
- **Quality Control**: Generates comprehensive QC reports.
- **Input/Output**: Accepts FASTQ files; outputs demultiplexed reads and reports.
- **Multi-sample Support**: Handles multiple samples in a single run.

## Pitfalls

- **Barcode Design**: Requires proper barcode design for successful demultiplexing.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal demultiplexing.
- **Data Quality**: Demultiplexing accuracy depends on input data quality.
- **Barcode Misassignment**: May occur with similar barcodes.

## Examples

### Demultiplex FASTQ files
**Args:** `mgikit demultiplex -i reads.fastq -b barcodes.txt -o demultiplexed/`
**Explanation:** Demultiplexes sequencing reads by barcodes.

### Generate QC report
**Args:** `mgikit qc -i reads.fastq -o qc_report.html`
**Explanation:** Generates quality control report.

### Paired-end demultiplexing
**Args:** `mgikit demultiplex -i reads_1.fastq -r reads_2.fastq -b barcodes.txt -o demultiplexed/`
**Explanation:** Demultiplexes paired-end sequencing data.

### Batch processing
**Args:** `mgikit batch -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.

### Custom barcode mismatches
**Args:** `mgikit demultiplex -i reads.fastq -b barcodes.txt -o demultiplexed/ -m 2`
**Explanation:** Allows 2 mismatches in barcode matching.