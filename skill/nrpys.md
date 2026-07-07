---
name: nrpys
category: programming
description: nrpys provides Python bindings for the nrps-rs substrate specificity predictor.
tags: [nrpys, programming, nrps, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/kblin/nrpys"
---

## Concepts

- **Tool Overview**: nrpys is a Python interface for nrps-rs natural product prediction.
- **Core Function**: Predicts substrate specificity for non-ribosomal peptide synthetases.
- **Algorithm**: Uses machine learning models for substrate prediction.
- **Input Format**: Accepts protein sequences or domain sequences.
- **Output**: Produces substrate specificity predictions.
- **Use Case**: Natural product discovery, NRPS analysis, and bioinformatics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Dependency**: Requires nrps-rs backend.
- **Model Accuracy**: Predictions may have varying accuracy.
- **Memory Usage**: Large datasets require memory.
- **Documentation**: Limited documentation.
- **Validation**: Results should be experimentally validated.

## Examples

### Install package
**Args:** `pip install nrpys`
**Explanation:** Installs nrpys package.

### Import module
**Args:** `import nrpys`
**Explanation:** Imports nrpys module.

### Predict substrate
**Args:** `result = nrpys.predict('ACDEFGHIKLMNPQRSTVWY')`
**Explanation:** Predicts substrate for peptide sequence.

### Batch prediction
**Args:** `results = nrpys.predict_batch(['seq1', 'seq2', 'seq3'])`
**Explanation:** Processes multiple sequences.

### Get probabilities
**Args:** `probs = nrpys.predict_proba('ACDEFGHIKLMNPQRSTVWY')`
**Explanation:** Returns prediction probabilities.

### Model info
**Args:** `info = nrpys.get_model_info()`
**Explanation:** Shows model information.

### Verbose mode
**Args:** `result = nrpys.predict('ACDEFGHIKLMNPQRSTVWY', verbose=True)`
**Explanation:** Runs with verbose output.