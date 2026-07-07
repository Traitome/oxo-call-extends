---
name: msisensor2
category: variant-calling
description: Machine learning-based MSI detection for tumor-only sequencing data including cfDNA and FFPE.
tags: [msisensor2, variant-calling, oncology]
author: oxo-call-community
source_url: "https://github.com/niu-lab/msisensor2"
---

## Concepts

- **Tool Overview**: MSIsensor2 v0.1 detects MSI using machine learning.
- **Core Function**: Identifies microsatellite instability from tumor-only data.
- **Machine Learning**: Uses ML algorithms for improved detection.
- **cfDNA Support**: Handles cell-free DNA samples.
- **FFPE Support**: Processes formalin-fixed paraffin-embedded samples.
- **Input/Output**: Accepts BAM files; outputs MSI status and scores.

## Pitfalls

- **Tumor-Only**: Designed for tumor-only sequencing data.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for detection.
- **Data Quality**: Results depend on sequencing quality.
- **Computational Resources**: Large datasets may require significant resources.
- **Model Training**: ML models may require training data.

## Examples

### Detect MSI in tumor-only data
**Args:** `msisensor2 msi -t tumor.bam -n normal_bases.list -o results.txt`
**Explanation:** Detects MSI from tumor-only BAM.

### With paired data
**Args:** `msisensor2 msi -t tumor.bam -n normal.bam -o results.txt`
**Explanation:** Uses paired tumor-normal for detection.

### Scan for repeat regions
**Args:** `msisensor2 scan -d reference.fa -o repeats.txt`
**Explanation:** Identifies microsatellite repeat regions.

### Generate report
**Args:** `msisensor2 msi -t tumor.bam -n normal_bases.list -r report.txt -o results.txt`
**Explanation:** Generates detailed detection report.

### Batch processing
**Args:** `msisensor2 msi -i bam/ -n normal_bases.list -o results/`
**Explanation:** Processes multiple tumor samples.