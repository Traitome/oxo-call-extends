---
name: bioemu
category: utility
description: Biomolecular emulator for protein equilibrium ensembles with generative deep learning
tags: [protein-structure, deep-learning, generative-model, ensemble]
author: oxo-call-community
source_url: "https://github.com/microsoft/bioemu"
---

## Concepts
- **Tool Overview**: BioEmu is a generative deep learning model for emulating protein equilibrium ensembles, predicting structural diversity of proteins.
- **Ensemble Prediction**: Generates diverse protein conformations representing equilibrium structural ensembles.
- **Deep Learning**: Uses diffusion-based generative models trained on protein structure data.
- **Applications**: Protein flexibility prediction, conformational sampling, drug design.

## Pitfalls
- **Model Accuracy**: Predicted ensembles are approximations; experimental validation recommended.
- **GPU Requirement**: Model inference benefits from GPU acceleration.

## Examples
### Generate protein ensemble
**Args:** `bioemu predict --sequence MKFLILLFNIL --num-samples 100 --output ensemble/`
**Explanation:** Generates 100 structural samples for a protein sequence.
