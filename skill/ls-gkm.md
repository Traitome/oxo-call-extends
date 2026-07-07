---
name: ls-gkm
category: utility
description: gkm-SVM, a sequence-based method for predicting regulatory DNA elements.
tags: [ls-gkm, utility, gkm-SVM, regulatory-elements]
author: oxo-call-community
source_url: "https://github.com/Dongwon-Lee/lsgkm"
---

## Concepts

- **Tool Overview**: ls-gkm v0.1.1 is a sequence-based method for predicting regulatory DNA elements using gapped k-mer Support Vector Machines (gkm-SVM).
- **Core Function**: Uses gapped k-mer features to train SVM models for predicting functional genomic regions.
- **Feature Extraction**: Extracts gapped k-mer features from DNA sequences for machine learning.
- **Input/Output**: Input: FASTA sequences, label files; Output: Model predictions, feature importance scores.
- **Installation**: `conda install -c bioconda ls-gkm`
- **Key Features**: Handles gapped k-mer patterns, efficient feature extraction, supports large-scale genomic data.

## Pitfalls

- **Computational Complexity**: Training on large datasets can be computationally intensive.
- **Memory Usage**: May require significant memory for large k-mer sizes or large datasets.
- **Parameter Tuning**: Requires careful tuning of k-mer size and SVM parameters.
- **Class Imbalance**: May struggle with imbalanced positive/negative training sets.
- **Interpretability**: Black-box model makes interpretation of results challenging.
- **Training Time**: Training on large datasets can be time-consuming.

## Examples

### Train model
**Args:** `gkmtrain -i sequences.fa -l labels.txt -o model.out`
**Explanation:** Trains a gkm-SVM model on input sequences with labels.

### Predict
**Args:** `gkmpredict -i test_sequences.fa -m model.out -o predictions.txt`
**Explanation:** Predicts labels for test sequences using trained model.

### Extract features
**Args:** `gkmexplain -i sequences.fa -m model.out -o features.txt`
**Explanation:** Extracts important features from trained model.

### K-mer size
**Args:** `gkmtrain -i sequences.fa -l labels.txt -k 10 -g 3 -o model.out`
**Explanation:** Uses k-mer size 10 with 3 gaps for feature extraction.

### Threads
**Args:** `gkmtrain -i sequences.fa -l labels.txt -t 8 -o model.out`
**Explanation:** Uses 8 threads for parallel processing.

### Help documentation
**Args:** `gkmtrain --help`
**Explanation:** Displays all available options and parameters.