---
name: qcumber
category: qc
description: QCumber performs quality control, quality trimming, adapter removal and sequence content check of NGS data.
tags: [qcumber, qc, trimming, adapter-removal]
author: oxo-call-community
source_url: "https://gitlab.com/RKIBioinformaticsPipelines/QCumber"
---

## Concepts

- **Tool Overview**: qcumber processes NGS data.
- **Core Function**: Quality control.
- **Algorithm**: Uses trimming algorithms.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces cleaned reads.
- **Use Case**: Preprocessing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Quality Threshold**: Must be set.
- **Adapter Sequences**: Must be known.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qcumber --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `qcumber run -i input.fastq -o cleaned.fastq`
**Explanation:** Runs QC and trimming.

### With parameters
**Args:** `qcumber run -i input.fastq -p params.yaml -o cleaned.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qcumber -v run -i input.fastq -o cleaned.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qcumber -t 4 run -i input.fastq -o cleaned.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Trim only
**Args:** `qcumber trim -i input.fastq -o trimmed.fastq`
**Explanation:** Performs only trimming.

### Generate report
**Args:** `qcumber run -i input.fastq -o cleaned.fastq --report report.html`
**Explanation:** Generates HTML report.