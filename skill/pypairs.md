---
name: pypairs
category: expression
description: pyPAIRS is a Python scRNA-Seq classifier using marker gene pairs.
tags: [pypairs, expression, single-cell, classification]
author: oxo-call-community
source_url: "https://pypairs.readthedocs.io/"
---

## Concepts

- **Tool Overview**: pypairs classifies scRNA-Seq.
- **Core Function**: Cell type classification.
- **Algorithm**: Uses marker pairs.
- **Input Format**: Accepts expression matrices.
- **Output**: Produces cell type predictions.
- **Use Case**: Single-cell analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Marker Selection**: Affects accuracy.
- **Data Normalization**: Must be consistent.
- **Runtime**: Classification may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pypairs --help`
**Explanation:** Shows available options and usage instructions.

### Classify cells
**Args:** `pypairs classify -i expression.h5ad -m markers.pkl -o predictions.txt`
**Explanation:** Predicts cell types.

### With parameters
**Args:** `pypairs classify -i expression.h5ad -p params.yaml -o predictions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pypairs -v classify -i expression.h5ad -o predictions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pypairs -t 4 classify -i expression.h5ad -o predictions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Train model
**Args:** `pypairs train -i training.h5ad -o markers.pkl`
**Explanation:** Trains marker pairs model.

### Generate report
**Args:** `pypairs classify -i expression.h5ad -o predictions.txt --report report.html`
**Explanation:** Generates HTML report.