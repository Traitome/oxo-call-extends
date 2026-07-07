---
name: qorts
category: expression
description: QoRTs is a toolkit for analysis, quality control, and data management of RNA-Seq datasets.
tags: [qorts, expression, rna-seq, quality-control]
author: oxo-call-community
source_url: "http://hartleys.github.io/QoRTs/"
---

## Concepts

- **Tool Overview**: qorts analyzes RNA-Seq data.
- **Core Function**: RNA-Seq QC.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces QC metrics.
- **Use Case**: RNA-Seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Annotation**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qorts --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `qorts run -i aligned.bam -o qc_report/`
**Explanation:** Runs RNA-Seq quality control.

### With parameters
**Args:** `qorts run -i aligned.bam -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qorts -v run -i aligned.bam -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qorts -t 4 run -i aligned.bam -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### Summarize
**Args:** `qorts summarize -i qc_report/ -o summary.txt`
**Explanation:** Summarizes QC results.

### Generate report
**Args:** `qorts run -i aligned.bam -o qc_report/ --report report.html`
**Explanation:** Generates HTML report.