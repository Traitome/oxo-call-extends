---
name: atol-qc-raw-ont
category: qc
description: AToL QC Raw ONT - Run read QC on Oxford Nanopore Technologies reads
tags: [nanopore, qc, long-reads, quality-control]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/atol-qc-raw-ont"
---

## Concepts

- **Tool Overview**: Quality control pipeline for Oxford Nanopore Technologies (ONT) raw reads as part of AToL Genome Engine workflow.

- **Read Statistics**: Calculates comprehensive statistics including read length distribution, quality scores, and yield metrics.

- **Adapter Detection**: Identifies and reports adapter sequences in reads.

- **Quality Filtering**: Filters reads based on quality scores and length thresholds.

## Pitfalls

- **Basecalling Version**: Results may vary depending on basecaller version used. Document basecalling parameters.

- **Flow Cell Quality**: Poor quality flow cells may have systematic errors affecting all reads.

- **Storage Requirements**: ONT datasets can be very large. Ensure sufficient disk space for processing.

## Examples

### Basic QC run
**Args:** `atol-qc-raw-ont --input reads.fastq.gz --output qc_results/`
**Explanation:** Runs quality control on ONT reads, generates statistics and filtered output.

### Filter by read length
**Args:** `atol-qc-raw-ont --input reads.fastq.gz --min-length 1000 --output filtered/`
**Explanation:** Filters reads to keep only those ≥1000bp.

### Quality filtering
**Args:** `atol-qc-raw-ont --input reads.fastq.gz --min-quality 10 --output high_quality/`
**Explanation:** Filters reads with average quality score ≥Q10.

### Generate QC report
**Args:** `atol-qc-raw-ont --input reads.fastq.gz --report qc_report.html --output results/`
**Explanation:** Generates HTML quality control report with visualizations.
