---
name: deeplift
category: annotation
description: DeepLIFT - computing importance scores in deep neural networks for model interpretation.
tags: [deeplift, annotation, deep-learning, interpretability, feature-importance]
author: oxo-call-community
source_url: "https://github.com/kundajelab/deeplift"
---

## Concepts

- **Tool Overview**: deeplift (v0.6.13.0+) implements algorithms for computing importance scores in deep neural networks, enabling interpretation of model predictions.
- **Core Function**: Computes feature importance scores by propagating activation differences through the network, identifying which input features contribute most to predictions.
- **Input/Output**: Input: Trained neural network model, input data. Output: Feature importance scores, visualization of important features.
- **Algorithm**: Implements methods from "Learning Important Features Through Propagating Activation Differences", including gradient-based and perturbation-based approaches.
- **Key Features**: Multiple importance scoring methods, supports various network architectures, visualization tools, integrates with Keras, provides attribution maps.
- **Installation**: `conda install -c bioconda deeplift`

## Pitfalls

- **Model Compatibility**: Requires compatible Keras/TensorFlow versions.
- **Computational Cost**: Can be computationally expensive for large models.
- **Interpretation Challenges**: Importance scores require careful interpretation.
- **Gradient Saturation**: May have issues with saturated activations.
- **Layer Compatibility**: Not all layer types are supported.

## Examples

### Compute importance scores
**Args:** `deeplift --model model.h5 --input data.npy --output scores.npy`
**Explanation:** Compute DeepLIFT importance scores for input features.

### With visualization
**Args:** `deeplift --model model.h5 --input data.npy --output scores.npy --visualize`
**Explanation:** Generate visualization of importance scores.

### Using specific method
**Args:** `deeplift --model model.h5 --input data.npy --method gradient --output scores.npy`
**Explanation:** Use gradient-based method for importance scoring.