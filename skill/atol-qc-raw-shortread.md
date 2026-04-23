---
name: atol-qc-raw-shortread
category: qc
description: AToL QC Raw Shortread - Run short read QC on Hi-C or other Illumina reads
tags: [illumina, short-reads, qc, hi-c]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/atol-qc-raw-shortread"
---

## Concepts

- **Tool Overview**: Quality control pipeline for Illumina short reads including Hi-C data in AToL Genome Engine workflow.

- **Standard QC Metrics**: Calculates standard quality metrics including per-base quality, GC content, and adapter contamination.

- **Hi-C Specific**: Includes checks for Hi-C library quality and junction detection.

- **Adapter Trimming**: Identifies and optionally removes adapter sequences.

## Pitfalls

- **Hi-C Artifacts**: Hi-C libraries may have specific artifacts (dangling ends, self-ligation) requiring special attention.

- **Contamination**: Short reads are susceptible to contamination. Check for unexpected organisms.

- **Duplication Rates**: High duplication rates may indicate PCR over-amplification.

## Examples

### Basic short read QC
**Args:** `atol-qc-raw-shortread --input R1.fastq.gz R2.fastq.gz --output qc_results/`
**Explanation:** Runs quality control on paired-end Illumina reads.

### Hi-C specific QC
**Args:** `atol-qc-raw-shortread --input hic_R1.fastq.gz hic_R2.fastq.gz --hic --output hic_qc/`
**Explanation:** Performs Hi-C-specific quality checks including junction analysis.

### Adapter trimming
**Args:** `atol-qc-raw-shortread --input R1.fastq.gz R2.fastq.gz --trim-adapters --output trimmed/`
**Explanation:** Identifies and removes adapter sequences from reads.

### Generate comprehensive report
**Args:** `atol-qc-raw-shortread --input R1.fastq.gz R2.fastq.gz --report qc_report.html --output results/`
**Explanation:** Generates detailed HTML report with all QC metrics and visualizations.
