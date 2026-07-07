---
name: dca
category: expression
description: Count autoencoder for single-cell RNA-seq denoising.
tags: [dca, expression, scRNA-seq, denoising, autoencoder, deep-learning]
author: oxo-call-community
source_url: "https://github.com/theislab/dca"
---

## Concepts

- **Tool Overview**: dca (v0.3.4+) is a deep learning tool for denoising single-cell RNA-seq data using a count autoencoder. It removes technical noise while preserving biological variation.
- **Core Function**: Denoises scRNA-seq count data by training an autoencoder network that learns to reconstruct true expression levels from noisy observations.
- **Input/Output**: Input: AnnData object or 10x format scRNA-seq data. Output: Denoised count matrix, latent representations, and trained model.
- **Algorithm**: Uses a count autoencoder with negative binomial noise model to learn a low-dimensional representation and reconstruct denoised counts.
- **Key Features**: Handles dropout events, preserves count nature of data, provides latent representations, supports batch correction.
- **Installation**: `conda install -c bioconda dca`

## Pitfalls

- **Computational Resources**: Requires GPU for efficient training on large datasets.
- **Hyperparameters**: Performance depends on network architecture and training parameters.
- **Overfitting**: May overfit on small datasets without proper regularization.
- **Batch Effects**: Requires explicit batch correction if strong batch effects present.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Basic denoising
**Args:** `dca input.h5ad output.h5ad`
**Explanation:** Denoise scRNA-seq data using default autoencoder architecture.

### Specify network architecture
**Args:** `dca input.h5ad output.h5ad --encoder-layers 512 256 --decoder-layers 256 512`
**Explanation:** Use custom encoder and decoder layer sizes.

### Train with batch correction
**Args:** `dca input.h5ad output.h5ad --batch-key batch`
**Explanation:** Perform denoising with batch correction using batch annotation.