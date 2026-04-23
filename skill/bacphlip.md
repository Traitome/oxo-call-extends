---
name: bacphlip
category: annotation
description: BACPHLIP - Random Forest classifier to predict bacteriophage lifestyle
tags: [phage, lifestyle-prediction, temperate, virulent, machine-learning]
author: oxo-call-community
source_url: "https://github.com/adamhockenberry/bacphlip"
---

## Concepts

- **Tool Overview**: BACPHLIP uses Random Forest classification to predict whether a bacteriophage has a temperate (lysogenic) or virulent (lytic) lifestyle based on protein sequence features.

- **Feature Extraction**: Extracts features from phage protein sequences to classify lifestyle without requiring experimental data.

- **Temperate vs Virulent**: Distinguishes between temperate phages (integrate into host genome) and virulent phages (strictly lytic).

- **Batch Processing**: Can classify multiple phage genomes simultaneously.

## Pitfalls

- **Prediction Accuracy**: Not 100% accurate. Some phages have ambiguous or mixed lifestyles.

- **Protein Prediction Required**: Requires protein predictions from phage genome. Use Prokka or similar tool first.

- **Novel Phages**: Very divergent phages may be misclassified due to lack of similar training examples.

- **Incomplete Genomes**: Fragmented or incomplete phage genomes may give unreliable predictions.

## Examples

### Predict single phage lifestyle
**Args:** `bacphlip predict --input phage_proteins.faa --output prediction.tsv`
**Explanation:** Predicts lifestyle from phage protein sequences in FASTA format.

### Batch prediction
**Args:** `bacphlip predict --input-dir phage_proteins/ --output predictions.tsv`
**Explanation:** Predicts lifestyles for all protein files in directory.

### From genome directly
**Args:** `bacphlip predict --genome phage.fasta --output prediction.tsv`
**Explanation:** Predicts lifestyle from phage genome, automatically predicting proteins first.

### Detailed output
**Args:** `bacphlip predict --input proteins.faa --verbose --output detailed_prediction.tsv`
**Explanation:** Provides detailed output including probability scores and feature importance.
