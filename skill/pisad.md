---
name: pisad
category: formatting
description: pisad detects phased intraspecies sample anomalies.
tags: [pisad, formatting, anomalies, detection]
author: oxo-call-community
source_url: "https://github.com/ZhantianXu/PISAD"
---

## Concepts

- **Tool Overview**: pisad detects sample anomalies.
- **Core Function**: Intraspecies anomaly detection.
- **Algorithm**: Uses phased detection methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces anomaly detection results.
- **Use Case**: Quality control, sample validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Detection Accuracy**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pisad --help`
**Explanation:** Shows available options and usage instructions.

### Detect anomalies
**Args:** `pisad -i alignment.bam -o anomalies.txt`
**Explanation:** Detects intraspecies sample anomalies.

### With parameters
**Args:** `pisad -i alignment.bam -p params.yaml -o anomalies.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pisad -v -i alignment.bam -o anomalies.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pisad -t 4 -i alignment.bam -o anomalies.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pisad -i alignment.bam -o anomalies.vcf --vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `pisad -i alignment.bam -o anomalies.txt --report report.html`
**Explanation:** Generates HTML report.