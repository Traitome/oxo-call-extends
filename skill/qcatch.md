---
name: qcatch
category: qc
description: QCatch is a quality control tool for downstream analysis of alevin-fry / simpleaf output.
tags: [qcatch, qc, quality-control, alevin-fry]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/QCatch"
---

## Concepts

- **Tool Overview**: qcatch performs QC checks.
- **Core Function**: Quality control.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts alevin-fry output.
- **Output**: Produces QC reports.
- **Use Case**: RNA-seq QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Input Format**: Must be correct.
- **Thresholds**: Must be configured.
- **Runtime**: QC may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qcatch --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `qcatch run -i alevin_output/ -o qc_report/`
**Explanation:** Runs quality control analysis.

### With parameters
**Args:** `qcatch run -i alevin_output/ -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qcatch -v run -i alevin_output/ -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qcatch -t 4 run -i alevin_output/ -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### Quick QC
**Args:** `qcatch quick -i alevin_output/ -o summary.txt`
**Explanation:** Runs quick QC check.

### Generate report
**Args:** `qcatch run -i alevin_output/ -o qc_report/ --report report.html`
**Explanation:** Generates HTML report.