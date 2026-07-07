---
name: scarches
category: single-cell
description: scArches - Transfer learning with Architecture Surgery on Single-cell data
tags: ["scarches", "single-cell", "transfer-learning", "deep-learning"]
author: oxo-call-community
source_url: "https://github.com/theislab/scarches"
---

## Concepts

- **Tool Overview**: scArches (v0.6.1) is a transfer learning framework for single-cell data analysis using Architecture Surgery.
- **Core Function**: Enables knowledge transfer between single-cell datasets for improved analysis.
- **Algorithm**: Uses neural network architecture modification for effective transfer learning.
- **Input/Output**: Accepts AnnData objects and produces integrated/transferred embeddings.
- **Domain Adaptation**: Adapts models from source to target domains effectively.
- **Applications**: Cell type annotation, cross-dataset integration, and batch effect removal.

## Pitfalls

- **Deep Learning Expertise**: Requires understanding of deep learning concepts.
- **Computational Resources**: High GPU requirements for training.
- **Data Quality**: Results depend on input data quality.
- **Training Time**: May require significant training time.
- **Parameter Tuning**: Requires careful adjustment of hyperparameters.
- **Model Complexity**: Complex models may be difficult to interpret.

## Examples

### Basic transfer learning
**Args:** `scarches train -i source.h5ad -t target.h5ad -o model.pt`
**Explanation:** `-i` source data; `-t` target data; `-o` output model.

### Cell type annotation
**Args:** `scarches annotate -i query.h5ad -m model.pt -o annotations.csv`
**Explanation:** Annotates cell types in query dataset using trained model.

### Model fine-tuning
**Args:** `scarches finetune -i data.h5ad -m model.pt -o finetuned.pt`
**Explanation:** Fine-tunes pre-trained model on new data.

### Integration
**Args:** `scarches integrate -i dataset1.h5ad dataset2.h5ad -o integrated.h5ad`
**Explanation:** Integrates multiple single-cell datasets.

### Latent representation
**Args:** `scarches embed -i data.h5ad -m model.pt -o embeddings.h5ad`
**Explanation:** Generates latent embeddings using trained model.

### Verbose logging
**Args:** `scarches train -i source.h5ad -t target.h5ad -v -o model.pt`
**Explanation:** `-v` enables verbose output for debugging.

### Hyperparameter tuning
**Args:** `scarches train -i source.h5ad -t target.h5ad --lr 0.001 -o model.pt`
**Explanation:** `--lr` sets learning rate for training.