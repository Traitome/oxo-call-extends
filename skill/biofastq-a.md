---
name: biofastq-a
category: qc
description: High-performance FASTQ/FASTA quality analysis tool written in Rust
tags: [fastq, quality-control, rust, adapter-trimming]
author: oxo-call-community
source_url: "https://github.com/DilaDeniz/BioFastq-a"
---

## Concepts
- **Tool Overview**: BioFastq-A is a fast, multi-threaded FASTQ/FASTA quality control tool written in Rust. It produces HTML reports, JSON output, adapter trimming, and various quality metrics.
- **QC Metrics**: Per-base quality, GC content, sequence length distribution, duplication levels, adapter content, k-mer analysis, N50/N90.
- **Features**: Adapter trimming, real-time terminal UI, per-tile quality analysis.
- **Performance**: Written in Rust for high speed and low memory usage.

## Pitfalls
- **Report Size**: HTML reports for large files can be large.
- **Adapter Database**: Adapter trimming requires known adapter sequences.

## Examples
### Generate QC report
**Args:** `biofastq-a -i reads.fq -o qc_report.html`
**Explanation:** Generates comprehensive quality control HTML report.

### Trim adapters
**Args:** `biofastq-a -i reads.fq --trim-adapters -o trimmed.fq`
**Explanation:** Trims adapters and generates QC report.

### Output JSON format
**Args:** `biofastq-a -i reads.fq -o results.json --format json`
**Explanation:** Outputs QC metrics in JSON format.
