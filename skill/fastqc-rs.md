---
name: fastqc-rs
category: qc
description: "A fast quality control tool for FASTQ files written in rust."
tags: [fastqc-rs, qc, quality-control, FASTQ, bioinformatics]
author: oxo-call-community
source_url: "https://fastqc-rs.github.io"
---

## Concepts

- **Tool Overview**: fastqc-rs is a fast quality control tool for FASTQ files written in Rust, providing quick quality assessment of sequencing data.
- **Core Function**: Performs quality control analysis on sequencing reads.
- **Input/Output**: Input: FASTQ files. Output: Quality reports, statistics, plots.
- **Algorithm**: Implements efficient parsing and quality assessment algorithms.
- **Key Features**: Fast processing, Rust implementation, comprehensive QC metrics, HTML reports, parallel processing.
- **Installation**: `conda install -c bioconda fastqc-rs`

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Format Compatibility**: Requires standard FASTQ format.
- **Data Quality**: Poor quality sequences may affect analysis.
- **Processing Time**: Very large files may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic QC analysis
**Args:** `fastqc-rs -i reads.fastq -o qc_report/`
**Explanation:** Generates quality control report.

### Parallel processing
**Args:** `fastqc-rs -i reads.fastq -o qc_report/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Multiple files
**Args:** `fastqc-rs -i reads1.fastq reads2.fastq -o qc_report/`
**Explanation:** Processes multiple FASTQ files.

### JSON output
**Args:** `fastqc-rs -i reads.fastq -o qc_report/ --json`
**Explanation:** Outputs metrics in JSON format.

### Quality threshold
**Args:** `fastqc-rs -i reads.fastq -o qc_report/ -q 20`
**Explanation:** Sets minimum quality threshold.