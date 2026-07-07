---
name: drevalpy
category: utility
description: "Drug response evaluation of cancer drug response models in a fair setting"
tags: [drevalpy, utility, drug-response, cancer, machine-learning]
author: oxo-call-community
source_url: "https://drevalpy.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Tool Overview**: DRevalPy is a Python package for evaluating cancer drug response prediction models in a fair and reproducible setting.
- **Core Function**: Provides standardized evaluation metrics and benchmarks for drug response prediction models.
- **Input/Output**: Input: Drug response data, model predictions. Output: Performance metrics, comparison reports.
- **Algorithm**: Implements various statistical metrics and fairness-aware evaluation methods.
- **Key Features**: Multiple evaluation metrics, cross-validation support, benchmark datasets, visualization tools.
- **Installation**: `conda install -c bioconda drevalpy`

## Pitfalls

- **Data Leakage**: Ensure proper train-test splitting to avoid data leakage.
- **Class Imbalance**: Uneven class distribution can affect metric interpretation.
- **Missing Data**: Missing drug response values require careful handling.
- **Model Selection**: Different models may require different evaluation approaches.
- **Threshold Selection**: Classification thresholds affect sensitivity/specificity trade-off.

## Examples

### Basic evaluation
**Args:** `--predictions pred.csv --true true.csv --output results.txt`
**Explanation:** Evaluates drug response predictions against true values.

### Cross-validation
**Args:** `--data data.csv --model model.pkl --output results.txt --cv 5`
**Explanation:** Performs 5-fold cross-validation evaluation.

### Multiple metrics
**Args:** `--predictions pred.csv --true true.csv --output results.txt --metrics AUC ACC F1`
**Explanation:** Computes multiple evaluation metrics (AUC, Accuracy, F1-score).

### Benchmark comparison
**Args:** `--predictions-dir submissions/ --true true.csv --output benchmark.txt`
**Explanation:** Compares multiple prediction models against benchmark.

### Fairness evaluation
**Args:** `--predictions pred.csv --true true.csv --groups groups.txt --output fairness.txt`
**Explanation:** Evaluates model fairness across different subgroups.