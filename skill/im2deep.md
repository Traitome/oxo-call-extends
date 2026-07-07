---
name: im2deep
category: programming
description: Framework for prediction of collisional cross-section of peptides.
tags: [im2deep, programming, proteomics, CCS, ion-mobility]
author: oxo-call-community
source_url: "https://github.com/compomics/im2deep"
---

## Concepts

- **Tool Overview**: im2deep (v1.2.0) - A deep learning framework for predicting collisional cross-section (CCS) values of peptide ions in ion mobility spectrometry
- **Core Function**: Uses deep neural networks to predict CCS values from peptide sequences, supporting modified peptides and multiconformational ions
- **Input/Output**: Accepts peptide sequences (with optional modifications), outputs predicted CCS values
- **Installation**: `conda install -c bioconda im2deep` or `pip install im2deep`
- **Key Features**: Atomic-level encoding, multi-output prediction for multiconformational peptides, transfer learning support

## Pitfalls

- **Modification Handling**: Requires proper formatting for post-translational modifications
- **Model Version**: Different model versions may produce different predictions
- **Peptide Length**: Performance may vary for extremely short or long peptides
- **Training Data Bias**: Models trained on specific datasets may not generalize to all peptide types
- **Computational Resources**: GPU recommended for large-scale predictions

## Examples

### Predict CCS for a single peptide
**Args:** `im2deep predict --sequence "PEPTIDE" --output result.csv`
**Explanation:** Predicts CCS value for the given peptide sequence.

### Batch prediction from file
**Args:** `im2deep predict --input peptides.txt --output predictions.csv`
**Explanation:** Processes multiple peptides from input file and generates predictions.

### Include modifications
**Args:** `im2deep predict --sequence "PEPTIDE[+80]" --modifications "M(ox)" --output result.csv`
**Explanation:** Predicts CCS for peptide with post-translational modifications.

### Train custom model
**Args:** `im2deep train --train_data train.csv --val_data val.csv --output model.h5`
**Explanation:** Trains a new CCS prediction model on custom dataset.

### Evaluate model performance
**Args:** `im2deep evaluate --model model.h5 --test_data test.csv`
**Explanation:** Evaluates model performance on test dataset.

### Generate feature importance
**Args:** `im2deep explain --sequence "PEPTIDE" --model model.h5 --output importance.png`
**Explanation:** Generates visualization of feature importance for prediction.