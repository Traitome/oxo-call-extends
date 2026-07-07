---
name: deeplc
category: annotation
description: DeepLC - retention time prediction for modified peptides using deep learning.
tags: [deeplc, annotation, proteomics, retention-time, mass-spectrometry]
author: oxo-call-community
source_url: "https://github.com/compomics/DeepLC/blob/v3.1.13/README.md"
---

## Concepts

- **Tool Overview**: deeplc (v3.1.13+) is a deep learning-based tool for predicting retention times of (modified) peptides in liquid chromatography-mass spectrometry (LC-MS).
- **Core Function**: Predicts peptide retention times based on sequence and modification information, improving peptide identification in proteomics.
- **Input/Output**: Input: Peptide sequences with modifications. Output: Predicted retention times, confidence scores.
- **Algorithm**: Uses deep neural networks trained on large datasets of peptide retention times to predict retention behavior.
- **Key Features**: Supports modified peptides, high accuracy, batch prediction, integrates with proteomics pipelines, transfer learning support.
- **Installation**: `conda install -c bioconda deeplc`

## Pitfalls

- **Modification Coverage**: May not support all peptide modifications.
- **Training Data**: Performance depends on training dataset diversity.
- **Instrument Specificity**: May need retraining for different LC systems.
- **Sequence Length**: May struggle with very long peptides.
- **Confidence Scores**: Interpretation of confidence scores requires care.

## Examples

### Predict retention times
**Args:** `deeplc -i peptides.csv -o predictions.csv`
**Explanation:** Predict retention times for peptides.

### With modifications
**Args:** `deeplc -i peptides_with_mods.csv -o predictions.csv`
**Explanation:** Predict retention times for modified peptides.

### Batch processing
**Args:** `deeplc -i peptides/ -o predictions/`
**Explanation:** Process multiple peptide files in batch.