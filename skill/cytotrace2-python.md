---
name: cytotrace2-python
category: expression
description: CytoTRACE 2 - interpretable AI method for predicting cellular potency from scRNA-seq data
tags: [cytotrace2-python, expression, scRNA-seq, single-cell, cellular-potency]
author: oxo-call-community
source_url: "https://github.com/digitalcytometry/cytotrace2/blob/v1.1.0/cytotrace2_python/README.md"
---

## Concepts

- **Tool Overview**: cytotrace2-python (v1.1.0+) is an interpretable AI method for predicting cellular potency and absolute developmental potential from scRNA-seq data.
- **Core Function**: Uses machine learning to infer cellular differentiation potential and predict cell fate trajectories.
- **Input/Output**: Input: Gene expression matrix (cells x genes). Output: Potency scores, cell rankings, trajectory predictions.
- **Algorithm**: Combines gene expression signatures with interpretable AI models for potency prediction.
- **Key Features**: Interpretable predictions, handles batch effects, supports various scRNA-seq technologies.
- **Installation**: `conda install -c bioconda cytotrace2-python`

## Pitfalls

- **Data Quality**: Requires high-quality scRNA-seq data with minimal dropout.
- **Normalization**: Proper data normalization is critical for accurate predictions.
- **Batch Effects**: Batch effects should be corrected before analysis.
- **Cell Type Diversity**: Works best with diverse cell populations spanning differentiation stages.
- **Interpretation**: Potency scores should be interpreted in context of experimental design.

## Examples

### Run CytoTRACE 2 on expression matrix
**Args:**
```python
import cytotrace2 as ct2
results = ct2.run_cytotrace(expression_matrix)
print(results['potency_scores'])
```
**Explanation:** Predict cellular potency from scRNA-seq expression matrix.

### Run with trajectory inference
**Args:**
```python
import cytotrace2 as ct2
results = ct2.run_cytotrace(expression_matrix, infer_trajectory=True)
print(results['trajectory_pseudotime'])
```
**Explanation:** Infer cellular potency along with developmental trajectory.

### Generate visualization
**Args:**
```python
import cytotrace2 as ct2
results = ct2.run_cytotrace(expression_matrix)
ct2.plot_potency(results, output_file='potency_plot.png')
```
**Explanation:** Generate visualization of potency scores.
