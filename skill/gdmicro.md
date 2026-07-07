---
name: gdmicro
category: machine-learning
description: GDmicro uses Graph Convolutional Networks (GCN) and Deep Adaptation Networks to classify host disease status based on human gut microbiome data.
tags: [gdmicro, microbiome, GCN, deep-learning, disease-classification]
author: oxo-call-community
source_url: "https://github.com/liaoherui/GDmicro"
---

## Concepts
- **Graph Convolutional Networks**: Uses GCN to model microbial interactions and community structure.
- **Deep Adaptation Network**: Implements domain adaptation for improved cross-dataset generalization.
- **Microbiome Classification**: Predicts host disease status from gut microbiome composition.
- **Transfer Learning**: Leverages knowledge transfer between different cohorts.
- **Taxonomic Profiling**: Works with taxonomic abundance data at various levels.

## Pitfalls
- **Data Quality**: Requires high-quality microbiome sequencing data.
- **Reference Databases**: Results depend on the choice of reference database (e.g., Greengenes, SILVA).
- **Batch Effects**: Batch effects can significantly impact classification performance.
- **Computational Resources**: Deep learning models require GPU acceleration.
- **Interpretability**: Black-box nature of deep learning models limits interpretability.

## Examples
### Train GDmicro model
**Args:** `gdmicro train -i microbiome_data.csv -l labels.txt -o model.pt -e 50`
**Explanation:** Trains a GDmicro model on microbiome data for 50 epochs.

### Predict disease status
**Args:** `gdmicro predict -i test_data.csv -m model.pt -o predictions.csv`
**Explanation:** Predicts disease status for new microbiome samples using a trained model.

### Cross-validation
**Args:** `gdmicro cv -i microbiome_data.csv -l labels.txt -k 5 -o results/`
**Explanation:** Performs 5-fold cross-validation to evaluate model performance.

### Feature importance
**Args:** `gdmicro explain -i sample.csv -m model.pt -o importance.txt`
**Explanation:** Generates feature importance scores for model interpretation.

### Fine-tune pre-trained model
**Args:** `gdmicro finetune -i new_data.csv -l new_labels.txt -m pretrained.pt -o finetuned.pt`
**Explanation:** Fine-tunes a pre-trained model on new dataset.