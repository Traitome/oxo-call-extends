---
name: preface
category: utility
description: preface predicts fetal component from sequencing data.
tags: [preface, utility, fetal, non-invasive]
author: oxo-call-community
source_url: "https://github.com/CenterForMedicalGeneticsGhent/PREFACE"
---

## Concepts

- **Tool Overview**: preface analyzes fetal fraction.
- **Core Function**: Fetal component prediction.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces fetal fraction estimates.
- **Use Case**: Non-invasive prenatal testing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Accuracy**: May have estimation errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `preface --help`
**Explanation:** Shows available options and usage instructions.

### Predict fetal component
**Args:** `preface -i reads.fastq -o fetal_fraction.txt`
**Explanation:** Predicts fetal component from data.

### With parameters
**Args:** `preface -i reads.fastq -p params.yaml -o fetal_fraction.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `preface -v -i reads.fastq -o fetal_fraction.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `preface -t 4 -i reads.fastq -o fetal_fraction.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `preface -i reads.fastq -o fetal_fraction.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `preface -i reads.fastq -o fetal_fraction.txt --report report.html`
**Explanation:** Generates HTML report.