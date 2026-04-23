---
name: basenji
category: annotation
description: Basenji - Sequential regulatory activity predictions with deep convolutional neural networks
tags: [regulatory-activity, deep-learning, cnn, epigenomics]
author: oxo-call-community
source_url: "https://github.com/calico/basenji"
---

## Concepts

- **Tool Overview**: Basenji predicts sequential regulatory activity from DNA sequence using deep convolutional neural networks, enabling functional annotation of non-coding regions.

- **CNN Architecture**: Uses dilated convolutional neural networks for capturing long-range regulatory interactions.

- **Multi-Task Learning**: Simultaneously predicts multiple epigenomic and transcriptomic signals.

- **Variant Scoring**: Can score the impact of genetic variants on regulatory activity.

- **Sequence-Based**: Predictions based solely on DNA sequence, no experimental data required for inference.

## Pitfalls

- **Model Training**: Training new models requires large epigenomic datasets and significant GPU resources.

- **Pre-trained Models**: Pre-trained models may not generalize across all cell types or organisms.

- **Variant Scoring**: Variant effect predictions are relative, not absolute. Interpret with caution.

- **Computational Requirements**: Inference on large genomes requires substantial memory.

## Examples

### Predict regulatory activity
**Args:** `basenji_predict.py -g genome.fasta -o predictions/ model/`
**Explanation:** Predicts regulatory activity across genome using pre-trained model.

### Score variant effects
**Args:** `basenji_var.py -g genome.fasta -v variants.vcf -o variant_scores/ model/`
**Explanation:** Scores the impact of genetic variants on regulatory activity.

### Saturation mutagenesis
**Args:** `basenji_sat.py -g genome.fasta -r chr1:1000-2000 -o saturation/ model/`
**Explanation:** Performs saturation mutagenesis on specified region to identify important positions.

### Train new model
**Args:** `basenji_train.py -d data_dir/ -p params.json -o model_output/`
**Explanation:** Trains new Basenji model on custom epigenomic dataset.
