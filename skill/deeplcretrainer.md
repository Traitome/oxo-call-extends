---
name: deeplcretrainer
category: annotation
description: Evaluating DeepLC performance and retraining prediction models.
tags: [deeplcretrainer, annotation, proteomics, machine-learning]
author: oxo-call-community
source_url: "https://github.com/RobbinBouwmeester/DeepLCRetrainer"
---

## Concepts

- **Tool Overview**: DeepLCRetrainer v1.0.2 - Tool for evaluating DeepLC performance and retraining prediction models for peptide retention time prediction.
- **Core Function**: Retrains DeepLC models to improve peptide retention time predictions for mass spectrometry proteomics.
- **Input/Output**: Expects peptide data files; outputs retrained models and evaluation metrics.
- **Installation**: `conda install -c bioconda deeplcretrainer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct peptide data format for training.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deeplcretrainer --input peptides.csv --output model/`
**Explanation:** Retrains DeepLC model with custom peptide data.
