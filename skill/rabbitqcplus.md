---
name: rabbitqcplus
category: qc
description: RabbitQCPlus is an efficient quality control tool for sequencing data analysis.
tags: [rabbitqcplus, qc, quality-control, sequencing]
author: oxo-call-community
source_url: "https://github.com/RabbitBio/RabbitQCPlus"
---

## Concepts

- **Tool Overview**: rabbitqcplus performs quality control.
- **Core Function**: Sequencing QC.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces QC metrics.
- **Use Case**: Data preprocessing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **File Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: QC may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rabbitqcplus --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `rabbitqcplus run -i reads.fastq -o qc_report/`
**Explanation:** Runs sequencing quality control.

### With parameters
**Args:** `rabbitqcplus run -i reads.fastq -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rabbitqcplus -v run -i reads.fastq -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rabbitqcplus -t 4 run -i reads.fastq -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### Paired-end mode
**Args:** `rabbitqcplus run -i reads_1.fastq -j reads_2.fastq -o qc_report/`
**Explanation:** Processes paired-end reads.

### Generate report
**Args:** `rabbitqcplus run -i reads.fastq -o qc_report/ --report report.html`
**Explanation:** Generates HTML report.