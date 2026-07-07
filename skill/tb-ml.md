---
name: tb-ml
category: machine-learning
description: Machine learning tools for tuberculosis research including prediction and classification models.
tags: [tb-ml, tuberculosis, machine-learning, prediction, classification, mycobacterium]
author: oxo-call-community
source_url: "https://github.com/jodyphelan/tb-ml"
---

## Concepts

- **Tool Overview**: tb-ml - Machine learning utilities for Mycobacterium tuberculosis research, including prediction models for drug resistance, lineage classification, and treatment outcome prediction.
- **Core Function**: Provides pre-trained ML models and training pipelines for TB genomic data analysis, including variant calling results as features.
- **Input**: VCF files or variant call tables from TB genome sequencing, with optional phenotypic data.
- **Output**: Predictions for drug resistance, lineage, or treatment outcomes with confidence scores.
- **Installation**: `pip install tb-ml` or `conda install -c bioconda tb-ml`
- **Use Case**: Predicting drug resistance phenotypes from genomic data without running phenotypic assays.

## Pitfalls

- **Model Version**: ML models are trained on specific datasets - ensure model version matches your population/setting.
- **Feature Requirements**: Models require specific variant positions - incomplete variant calling may reduce accuracy.
- **Database Updates**: Drug resistance mutations evolve - models need periodic retraining with updated data.
- **Interpretation**: Predictions are probabilistic - always confirm critical results phenotypically.

## Examples

### List available models
**Args:** `tb-ml list`
**Explanation:** Display all available pre-trained models for prediction.

### Predict drug resistance
**Args:** `tb-ml predict --model drug_resistance --input variants.vcf`
**Explanation:** Predict drug resistance phenotypes from variant call file.

### Lineage classification
**Args:** `tb-ml predict --model lineage --input sample.vcf`
**Explanation:** Classify M. tuberculosis lineage from genomic variants.

### Train custom model
**Args:** `tb-ml train --data training_set.tsv --labels labels.csv --output model.pkl`
**Explanation:** Train a custom model on your own dataset with known phenotypes.
