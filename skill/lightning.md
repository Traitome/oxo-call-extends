---
name: lightning
category: machine-learning
description: lightning - Large-scale linear classification, regression and ranking in Python
tags: [lightning, machine-learning, python, classification, regression, ranking]
author: oxo-call-community
source_url: "http://contrib.scikit-learn.org/lightning/"
---

## Concepts

- **Linear Classification**: Large-scale linear classification algorithms
- **Linear Regression**: Linear regression for predictive modeling
- **Ranking**: Learning to rank algorithms
- **Python Library**: Python-based machine learning library
- **Scalability**: Designed for large-scale datasets
- **scikit-learn Integration**: Compatible with scikit-learn ecosystem

## Pitfalls

- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Feature Scaling**: Features need proper scaling
- **Model Selection**: Appropriate model selection is critical
- **Version Compatibility**: API may change between versions
- **Documentation**: Limited documentation compared to scikit-learn

## Examples

### Train linear classifier
**Args:** `python -c "from lightning.classification import SGDClassifier; clf = SGDClassifier(); clf.fit(X, y)"`
**Explanation:** Trains linear classifier using stochastic gradient descent.

### Linear regression
**Args:** `python -c "from lightning.regression import SGDRegressor; reg = SGDRegressor(); reg.fit(X, y)"`
**Explanation:** Trains linear regression model.

### Ranking SVM
**Args:** `python -c "from lightning.ranking import SVMRank; ranker = SVMRank(); ranker.fit(X, y)"`
**Explanation:** Trains ranking SVM model.

### Multi-class classification
**Args:** `python -c "from lightning.classification import SGDClassifier; clf = SGDClassifier(multi_class='ovr'); clf.fit(X, y)"`
**Explanation:** Performs multi-class classification using one-vs-rest.

### Logistic regression
**Args:** `python -c "from lightning.classification import SGDClassifier; clf = SGDClassifier(loss='log'); clf.fit(X, y)"`
**Explanation:** Trains logistic regression model.

### Model persistence
**Args:** `python -c "import joblib; joblib.dump(clf, 'model.pkl')"`
**Explanation:** Saves trained model to disk.