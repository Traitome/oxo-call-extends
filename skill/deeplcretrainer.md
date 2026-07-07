---
name: deeplcretrainer
category: annotation
description: DeepLCRetrainer - evaluating and retraining DeepLC retention time prediction models.
tags: [deeplcretrainer, annotation, proteomics, model-retraining, machine-learning]
author: oxo-call-community
source_url: "https://github.com/RobbinBouwmeester/DeepLCRetrainer"
---

## Concepts

- **Tool Overview**: deeplcretrainer (v1.0.2+) is a tool for evaluating DeepLC performance and retraining prediction models for peptide retention time prediction in proteomics.
- **Core Function**: Evaluates existing DeepLC models and retrains them on custom datasets to improve retention time prediction accuracy.
- **Input/Output**: Input: Peptide data with measured retention times, existing model (optional). Output: Retrained model, evaluation metrics, performance reports.
- **Algorithm**: Uses transfer learning to adapt pre-trained DeepLC models to custom datasets, with evaluation metrics for model performance.
- **Key Features**: Model evaluation, transfer learning, custom training, performance metrics, supports various peptide modifications.
- **Installation**: `conda install -c bioconda deeplcretrainer`

## Pitfalls

- **Data Quality**: Requires high-quality training data with accurate retention times.
- **Dataset Size**: May need large datasets for effective retraining.
- **Computational Resources**: Requires significant computational resources.
- **Model Compatibility**: Requires compatible DeepLC model versions.
- **Overfitting Risk**: May overfit to training data if not properly regularized.

## Examples

### Retrain DeepLC model
**Args:** `deeplcretrainer --input peptides.csv --output model/`
**Explanation:** Retrain DeepLC model with custom peptide data.

### Evaluate existing model
**Args:** `deeplcretrainer --evaluate --model existing_model.h5 --input test_data.csv`
**Explanation:** Evaluate performance of existing model.

### Fine-tune with transfer learning
**Args:** `deeplcretrainer --input peptides.csv --output model/ --transfer-learning`
**Explanation:** Use transfer learning for model fine-tuning.