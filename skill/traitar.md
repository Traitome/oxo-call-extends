---
name: traitar
category: analysis
description: Traitar - Tool for trait prediction from genome sequences.
tags: [traitar, trait-prediction, genomics, phenotype, machine-learning]
author: oxo-call-community
source_url: "https://github.com/compbio/traitar"
---

## Concepts

- **Tool Overview**: Traitar - A tool for predicting phenotypic traits from genome sequences using machine learning.
- **Core Function**: Uses trained classifiers to predict traits based on genomic features.
- **Input**: Genome sequences (FASTA), feature annotations.
- **Output**: Predicted traits, confidence scores, feature importance.
- **Installation**: `pip install traitar` or `conda install -c bioconda traitar`
- **Use Case**: Phenotype prediction, microbial characterization, functional genomics.

## Pitfalls

- **Training Data**: Model performance depends on training data quality.
- **Feature Selection**: Requires appropriate feature selection for accurate predictions.

## Examples

### Predict traits
**Args:** `traitar predict -i genome.fasta -o predictions/`
**Explanation:** Predict phenotypic traits from genome sequence.

### Train model
**Args:** `traitar train -i training_data/ -o model.pkl`
**Explanation:** Train custom trait prediction model.
