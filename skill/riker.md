---
name: riker
category: qc
description: Riker performs high-performance NGS quality control.
tags: [riker, qc, ngs, quality-control]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/riker/blob/v0.1.0/README.md"
---

## Concepts

- **Tool Overview**: riker performs NGS QC.
- **Core Function**: Quality control analysis.
- **Algorithm**: Uses high-performance methods.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces QC metrics.
- **Use Case**: Quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Affects QC.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `riker --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `riker qc -i reads.fastq -o qc_report/`
**Explanation:** Performs NGS quality control.

### With parameters
**Args:** `riker qc -i reads.fastq -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `riker -v qc -i reads.fastq -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `riker -t 4 qc -i reads.fastq -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### With adapter trimming
**Args:** `riker qc -i reads.fastq --trim -o qc_report/`
**Explanation:** Enables adapter trimming.

### Generate plots
**Args:** `riker qc -i reads.fastq -o qc_report/ --plots`
**Explanation:** Generates QC plots.