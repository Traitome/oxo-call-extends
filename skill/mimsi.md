---
name: mimsi
category: utility
description: A Deep Multiple Instance Learning Classifier for Microsatellite Instability
tags: [mimsi, utility, cancer]
author: oxo-call-community
source_url: "https://github.com/mskcc/mimsi"
---

## Concepts

- **Tool Overview**: MiMSI v0.4.5 classifies microsatellite instability using deep learning.
- **Core Function**: Classifies microsatellite instability status from sequencing data.
- **Microsatellite Instability**: Detects MSI in tumor samples.
- **Deep Learning**: Uses multiple instance learning for classification.
- **Input/Output**: Accepts sequencing data; outputs MSI classification.
- **Cancer Diagnosis**: Supports cancer genomic analysis.

## Pitfalls

- **Deep Learning Dependency**: Requires TensorFlow/PyTorch.
- **Computational Resources**: Classification requires significant resources.
- **Memory Requirements**: Memory usage can be high for model loading.
- **Model Training**: Requires trained model for classification.
- **Data Quality**: Classification accuracy depends on input data quality.
- **Cancer Specific**: Designed for tumor sequencing data.

## Examples

### Classify MSI status
**Args:** `mimsi -i tumor.bam -o result.txt`
**Explanation:** Classifies microsatellite instability status.

### With normal sample
**Args:** `mimsi -i tumor.bam -n normal.bam -o result.txt`
**Explanation:** Uses matched normal sample for comparison.

### Detailed output
**Args:** `mimsi -i tumor.bam -o result.txt -v`
**Explanation:** Generates detailed classification report.

### Batch processing
**Args:** `mimsi -i bam/ -o results/`
**Explanation:** Processes multiple tumor samples in batch mode.

### Confidence score
**Args:** `mimsi -i tumor.bam -o result.txt -c`
**Explanation:** Outputs confidence scores for classification.