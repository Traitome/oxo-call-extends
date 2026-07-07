---
name: qcli
category: qc
description: QCLI is a command-line interface tool for quality control operations.
tags: [qcli, qc, command-line, utility]
author: oxo-call-community
source_url: "https://pypi.org/project/qcli/"
---

## Concepts

- **Tool Overview**: qcli provides QC utilities.
- **Core Function**: Quality control.
- **Algorithm**: Uses various methods.
- **Input Format**: Accepts sequence files.
- **Output**: Produces QC metrics.
- **Use Case**: Data QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **File Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qcli --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `qcli run -i input.fastq -o qc_report/`
**Explanation:** Runs quality control analysis.

### With parameters
**Args:** `qcli run -i input.fastq -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qcli -v run -i input.fastq -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qcli -t 4 run -i input.fastq -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### Quick check
**Args:** `qcli quick -i input.fastq -o summary.txt`
**Explanation:** Runs quick QC check.

### Generate report
**Args:** `qcli run -i input.fastq -o qc_report/ --report report.html`
**Explanation:** Generates HTML report.