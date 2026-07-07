---
name: immuneml
category: utility
description: immuneML is a software platform for machine learning analysis of immune receptor repertoires.
tags: [immuneml, utility, machine-learning, immunology, repertoires]
author: oxo-call-community
source_url: "https://docs.immuneml.uio.no"
---

## Concepts

- **Tool Overview**: immuneml (v3.0.21) - A machine learning platform for analyzing immune receptor repertoire data
- **Core Function**: Provides tools for preprocessing, feature extraction, ML model training, and interpretation of immune repertoire data
- **Input/Output**: Accepts various immune repertoire formats (AIRR, IMGT, etc.), outputs trained models and analysis reports
- **Installation**: `conda install -c bioconda immuneml` or from GitHub
- **Key Features**: Supports TCR/BCR analysis, built-in ML models, explainable AI, reproducible pipelines

## Pitfalls

- **Data Format**: Requires standardized input formats; non-standard formats need conversion
- **Memory Requirements**: Large repertoire datasets require significant memory
- **Feature Selection**: Appropriate feature selection critical for model performance
- **Class Imbalance**: Unequal class distribution affects model training
- **Computational Time**: Complex ML pipelines can be time-consuming

## Examples

### Run basic analysis pipeline
**Args:** `immune-ml run_config.yaml -o results/`
**Explanation:** Executes analysis pipeline defined in YAML configuration file.

### Preprocess repertoire data
**Args:** `immune-ml preprocess -i data/ -o preprocessed/ -f airr`
**Explanation:** Preprocesses raw repertoire data into standardized format.

### Train ML model
**Args:** `immune-ml train -i preprocessed/ -m random_forest -o model/`
**Explanation:** Trains random forest model on repertoire data.

### Evaluate model performance
**Args:** `immune-ml evaluate -m model/ -i test_data/ -o evaluation/`
**Explanation:** Evaluates trained model on test dataset.

### Generate interpretability report
**Args:** `immune-ml interpret -m model/ -i data/ -o interpretation/`
**Explanation:** Generates explainability report for model predictions.

### Convert data format
**Args:** `immune-ml convert -i raw_data/ -f imgt -t airr -o converted/`
**Explanation:** Converts IMGT format data to AIRR format.