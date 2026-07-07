---
name: qualifilter
category: qc
description: QualiFilter generates QC reports summarizing key quality metrics and sample pass/fail status according to user-defined thresholds.
tags: [qualifilter, qc, quality-control, reporting]
author: oxo-call-community
source_url: "https://github.com/buhlentozini/QualiFilter"
---

## Concepts

- **Tool Overview**: qualifilter filters by quality.
- **Core Function**: QC filtering.
- **Algorithm**: Uses quality metrics.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces QC reports.
- **Use Case**: Quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Thresholds**: Must be configured.
- **Metrics**: Must be defined.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qualifilter --help`
**Explanation:** Shows available options and usage instructions.

### Run QC filtering
**Args:** `qualifilter run -i reads.fastq -o qc_report/`
**Explanation:** Generates quality report.

### With parameters
**Args:** `qualifilter run -i reads.fastq -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qualifilter -v run -i reads.fastq -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qualifilter -t 4 run -i reads.fastq -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### With thresholds
**Args:** `qualifilter run -i reads.fastq -q 20 -o qc_report/`
**Explanation:** Uses quality threshold.

### Generate report
**Args:** `qualifilter run -i reads.fastq -o qc_report/ --report report.html`
**Explanation:** Generates HTML report.