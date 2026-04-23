---
name: deeplift
category: annotation
description: DeepLIFT (Deep Learning Important FeaTures) - Algorithms for computing importance scores in deep neural networks.
tags: [deeplift, annotation, deep-learning, interpretability]
author: oxo-call-community
source_url: "https://github.com/kundajelab/deeplift"
---

## Concepts

- **Tool Overview**: DeepLIFT v0.6.13.0 - Algorithms for computing importance scores in deep neural networks. Implements methods from "Learning Important Features Through Propagating Activation Differences".
- **Core Function**: Computes feature importance scores for deep neural network predictions using methods like gradients, guided backprop, and integrated gradients.
- **Input/Output**: Expects trained Keras models and input data; outputs importance scores per feature.
- **Installation**: `conda install -c bioconda deeplift`

## Pitfalls

- **Version Differences**: Requires compatible Keras/Theano versions.
- **Input Format**: Ensure model and data format compatibility with the library.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `deeplift --model model.h5 --input data.npy --output scores.npy`
**Explanation:** Computes DeepLIFT importance scores for input features.
