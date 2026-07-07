---
name: libsvm
category: machine-learning
description: LIBSVM - Support Vector Machine library for classification and regression
tags: [libsvm, machine-learning, SVM, classification, regression]
author: oxo-call-community
source_url: "https://www.csie.ntu.edu.tw/~cjlin/libsvm/"
---

## Concepts

- **Support Vector Machines**: SVM classification and regression
- **Kernel Methods**: Various kernel functions (linear, RBF, polynomial)
- **Classification**: Binary and multi-class classification
- **Regression**: Support vector regression
- **Model Training**: Training SVM models from data
- **Cross-Validation**: Model evaluation using cross-validation

## Pitfalls

- **Parameter Tuning**: Requires careful parameter optimization
- **Scaling**: Features need proper scaling
- **Memory Usage**: Memory-intensive for large datasets
- **Training Time**: May be slow for large datasets
- **Kernel Selection**: Appropriate kernel selection is critical
- **Class Imbalance**: Imbalanced data affects results

## Examples

### Train classifier
**Args:** `svm-train -s 0 -t 2 -c 1 input.txt model.svm`
**Explanation:** Trains SVM classifier with RBF kernel.

### Predict labels
**Args:** `svm-predict test.txt model.svm output.txt`
**Explanation:** Predicts labels using trained model.

### Cross-validation
**Args:** `svm-train -v 5 -s 0 input.txt`
**Explanation:** Performs 5-fold cross-validation.

### Regression
**Args:** `svm-train -s 3 -t 2 -c 1 data.txt model.svm`
**Explanation:** Trains SVM regression model.

### Grid search
**Args:** `svm-grid.py input.txt`
**Explanation:** Performs grid search for parameter optimization.

### Model statistics
**Args:** `svm-stat model.svm`
**Explanation:** Shows model statistics.