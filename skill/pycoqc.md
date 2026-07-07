---
name: pycoqc
category: qc
description: PycoQC computes metrics and generates interactive QC plots for Oxford Nanopore sequencing data quality control.
tags: [pycoqc, qc, nanopore, quality-control]
author: oxo-call-community
source_url: "https://a-slide.github.io/pycoQC/"
---

## Concepts

- **Tool Overview**: pycoqc performs QC analysis.
- **Core Function**: Sequencing quality control.
- **Algorithm**: Uses statistics and visualization.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces QC reports.
- **Use Case**: Nanopore sequencing QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **File Compatibility**: May have format issues.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pycoqc --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `pycoqc -i sequencing_summary.txt -o qc_report.html`
**Explanation:** Generates QC report from sequencing summary.

### With parameters
**Args:** `pycoqc -i sequencing_summary.txt -p params.yaml -o qc_report.html`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pycoqc -v -i sequencing_summary.txt -o qc_report.html`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pycoqc -t 4 -i sequencing_summary.txt -o qc_report.html`
**Explanation:** Uses 4 threads for parallel processing.

### From FASTQ
**Args:** `pycoqc -f reads.fastq -o qc_report.html`
**Explanation:** Generates QC from FASTQ files.

### Generate report
**Args:** `pycoqc -i sequencing_summary.txt -o qc_report.html --report detailed.html`
**Explanation:** Generates detailed HTML report.