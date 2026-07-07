---
name: mqc
category: qc
description: Quality control tool to assess mapping quality of ribosome profiling experiments.
tags: [mqc, qc, ribosome-profiling]
author: oxo-call-community
source_url: "https://github.com/Biobix/mQC"
---

## Concepts

- **Tool Overview**: mQC v1.10 assesses mapping quality of ribosome profiling experiments.
- **Core Function**: Performs quality control for ribosome profiling data.
- **Ribosome Profiling**: Specialized for Ribo-seq data analysis.
- **Mapping Quality**: Evaluates read mapping quality metrics.
- **QC Metrics**: Computes various quality control metrics.
- **Input/Output**: Accepts BAM files; outputs QC reports and metrics.

## Pitfalls

- **Ribo-seq Specific**: Designed for ribosome profiling data.
- **Memory Requirements**: Memory usage depends on BAM size.
- **Parameter Tuning**: May require parameter adjustment for QC.
- **Data Quality**: Results depend on sequencing and mapping quality.
- **BAM Required**: Requires aligned reads in BAM format.
- **Computational Resources**: Large BAMs may require significant resources.

## Examples

### Run quality control
**Args:** `mqc -i alignments.bam -o qc_report.html`
**Explanation:** Performs QC on ribosome profiling data.

### With multiple samples
**Args:** `mqc -i bam/ -o qc_reports/`
**Explanation:** Processes multiple BAM files.

### Generate metrics only
**Args:** `mqc -i alignments.bam -m -o metrics.txt`
**Explanation:** Outputs QC metrics without report.

### With custom thresholds
**Args:** `mqc -i alignments.bam -t thresholds.yaml -o qc_report.html`
**Explanation:** Uses custom QC thresholds.

### Compare samples
**Args:** `mqc compare -i qc_reports/ -o comparison.html`
**Explanation:** Compares QC metrics across samples.