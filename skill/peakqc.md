---
name: peakqc
category: expression
description: PEAKQC provides quality control for single cell ATAC-seq data.
tags: [peakqc, expression, atac-seq, single-cell]
author: oxo-call-community
source_url: "https://github.com/loosolab/PEAKQC"
---

## Concepts

- **Tool Overview**: PEAKQC performs ATAC-seq QC.
- **Core Function**: Evaluates quality based on fragment length.
- **Algorithm**: Uses fragment distribution analysis.
- **Input Format**: Accepts single cell ATAC-seq data.
- **Output**: Produces QC metrics and reports.
- **Use Case**: Single cell ATAC-seq, quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Fragment Analysis**: Requires proper fragment data.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peakqc --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `peakqc -i fragments.tsv -o qc_report.html`
**Explanation:** Performs quality control analysis.

### With thresholds
**Args:** `peakqc -i fragments.tsv --min-fragments 1000 -o qc_report.html`
**Explanation:** Sets minimum fragment threshold.

### Verbose mode
**Args:** `peakqc -v -i fragments.tsv -o qc_report.html`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peakqc -t 4 -i fragments.tsv -o qc_report.html`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peakqc -i fragments.tsv -o qc_metrics.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peakqc -i fragments.tsv -o qc_report.html --report`
**Explanation:** Generates HTML report.