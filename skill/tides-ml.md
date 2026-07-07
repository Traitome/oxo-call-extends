---
name: tides-ml
category: analysis
description: TIDES-ML - Tandem repeat detection using machine learning.
tags: [tides-ml, tandem-repeat, machine-learning, long-read, repeat-detection]
author: oxo-call-community
source_url: "https://github.com/compbio/tides-ml"
---

## Concepts

- **Tool Overview**: TIDES-ML (Tandem repeat Detector using Machine Learning) - A machine learning-based tool for detecting tandem repeats in long-read sequencing data.
- **Core Function**: Uses trained ML models to distinguish true tandem repeats from sequencing artifacts in noisy long reads.
- **Input**: Long-read sequencing data (FASTQ), optionally with training labels.
- **Output**: Tandem repeat predictions with confidence scores, repeat unit annotations.
- **Installation**: `pip install tides-ml` or `conda install -c bioconda tides-ml`
- **Use Case**: Accurate tandem repeat detection in noisy data, repeat expansion research.

## Pitfalls

- **Model Training**: Pre-trained models may need fine-tuning for specific organisms.
- **Long Reads**: Designed for long-read data only.

## Examples

### Detect repeats with ML
**Args:** `tides-ml -i long_reads.fastq.gz -o ml_repeat_predictions/`
**Explanation:** Use ML model to detect tandem repeats.

### With custom model
**Args:** `tides-ml -i reads.fastq -m custom_model.pkl -o results/`
**Explanation:** Apply custom-trained model for repeat detection.
