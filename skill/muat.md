---
name: muat
category: variant-calling
description: A package for Mutation Attention Tool
tags: [muat, variant-calling, deep-learning, tumor-typing, mutation-analysis]
author: oxo-call-community
source_url: "https://github.com/primasanjaya/muat"
---

## Concepts

- **Tool Overview**: MuAt (Mutation Attention) v0.1.17 is a deep neural network model for tumor type prediction.
- **Core Function**: Predicts tumor types and subtypes from somatic mutations using attention-based DNN.
- **Input**: Accepts VCF files containing SNVs, MNVs, InDels, and structural variants.
- **Output**: Provides tumor type classifications with confidence scores.
- **Methodology**: Uses three-module architecture with attention mechanism for mutation feature weighting.
- **Performance**: Achieves 88.8% accuracy on PCAWG whole-genome data (24 tumor types).

## Pitfalls

- **Mutation Burden**: Limited performance for tumors with low mutation负荷.
- **Data Format**: Requires properly formatted mutation data (VCF or similar).
- **Training Data**: Model performance depends on training data diversity.
- **Computational Resources**: DNN training and inference require GPU resources.
- **Sample Quality**: Results depend on mutation calling quality from upstream pipelines.
- **Subtype Specificity**: May have reduced accuracy for rare tumor subtypes.

## Examples

### Predict tumor type
**Args:** `muat predict -i mutations.vcf -o prediction.txt`
**Explanation:** Predicts tumor type from mutation VCF file.

### Batch processing
**Args:** `muat batch -d mutation_dir/ -o results/`
**Explanation:** Processes multiple samples in batch mode.

### Train custom model
**Args:** `muat train -i training_data/ -o model_out/ -e 50`
**Explanation:** Trains model for 50 epochs on custom dataset.

### Display help
**Args:** `muat --help`
**Explanation:** Shows all available commands and options.

### Extract mutation features
**Args:** `muat extract -i variants.vcf -o features.tsv`
**Explanation:** Extracts mutation features for downstream analysis.
