---
name: sloika
category: nanopore-analysis
description: Sloika is Oxford Nanopore Technologies' software for training neural network models for base calling
tags: [sloika, nanopore, basecalling, neural-network, deep-learning]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/sloika"
---

## Concepts

- **Tool Overview**: sloika (v2.0.1) - Oxford Nanopore's neural network training framework for base calling
- **Core Function**: Trains deep learning models for raw signal to DNA sequence conversion
- **Input/Output**: Accepts raw nanopore signal data; outputs trained base calling models
- **Algorithm**: Uses recurrent neural networks (RNN) for sequence prediction
- **Installation**: `conda install -c bioconda sloika`
- **Key Features**: Supports custom model architectures, transfer learning, and model evaluation

## Pitfalls

- **GPU Requirements**: Training requires GPU resources
- **Data Preparation**: Raw signal data must be properly preprocessed
- **Training Time**: Model training can be time-consuming
- **Memory Usage**: Large datasets require significant GPU memory
- **Model Complexity**: Tuning hyperparameters requires expertise
- **Nanopore Specific**: Designed specifically for Oxford Nanopore data

## Examples

### Display help
**Args:** `sloika --help`
**Explanation:** Shows available options and usage information.

### Train base calling model
**Args:** `sloika train -i training_data/ -o model_output/ -c config.json`
**Explanation:** Train a neural network model for base calling.

### Evaluate model
**Args:** `sloika evaluate -m model.h5 -i test_data/ -o metrics.txt`
**Explanation:** Evaluate trained model performance on test data.

### Predict sequences
**Args:** `sloika predict -m model.h5 -i raw_signal.fast5 -o predictions.fasta`
**Explanation:** Use trained model to base call raw signal data.

### Fine-tune model
**Args:** `sloika train -i new_data/ -o fine_tuned_model/ -m pre-trained.h5`
**Explanation:** Fine-tune an existing model with new data.

### Extract features
**Args:** `sloika extract -i raw_signal.fast5 -o features.h5`
**Explanation:** Extract features from raw signal for model training.

### Generate training data
**Args:** `sloika prepare -i reads.fast5 -r reference.fasta -o training_data/`
**Explanation:** Prepare labeled training data from reads and reference.