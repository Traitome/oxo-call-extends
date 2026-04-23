---
name: biobb_pytorch
category: utility
description: BioBB module for creating and training ML & DL models using PyTorch
tags: [bioexcel, pytorch, deep-learning, building-blocks]
author: oxo-call-community
source_url: "https://github.com/bioexcel/biobb_pytorch"
---

## Concepts
- **Tool Overview**: biobb_pytorch provides BioExcel Building Blocks for creating and training machine learning and deep learning models using PyTorch.
- **DL Models**: Supports neural network creation, training, inference, and model evaluation.
- **Applications**: Protein property prediction, structure prediction, drug discovery, bioimage analysis.

## Pitfalls
- **GPU Dependency**: Training large models benefits from GPU acceleration.
- **Data Requirements**: Deep learning requires substantial training data.

## Examples
### Train a model
**Args:** `biobb_pytorch.train --config train.yml --data dataset/ --output model.pt`
**Explanation:** Trains a PyTorch model using specified configuration.

### Run inference
**Args:** `biobb_pytorch.infer --model model.pt --input features.csv --output predictions.csv`
**Explanation:** Makes predictions using a trained PyTorch model.
