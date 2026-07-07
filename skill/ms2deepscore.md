---
name: ms2deepscore
category: utility
description: Deep learning similarity measure for comparing MS/MS spectra by chemical similarity.
tags: [ms2deepscore, utility, proteomics]
author: oxo-call-community
source_url: "https://github.com/matchms/ms2deepscore"
---

## Concepts

- **Tool Overview**: MS2DeepScore v2.7.2 uses deep learning for MS/MS spectrum comparison.
- **Core Function**: Predicts molecular similarity from mass spectrometry spectra.
- **Siamese Network**: Uses neural network architecture for similarity learning.
- **Tanimoto Score**: Predicts structural similarity scores.
- **Mass Spectrometry**: Specialized for MS/MS data analysis.
- **Input/Output**: Accepts MS/MS spectra; outputs similarity scores.

## Pitfalls

- **MS/MS Specific**: Designed for mass spectrometry data.
- **Model Training**: Requires training on labeled data.
- **Memory Requirements**: Neural network inference requires resources.
- **Parameter Tuning**: May require parameter adjustment for predictions.
- **Data Quality**: Results depend on spectrum quality.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Compute spectrum similarity
**Args:** `ms2deepscore -i spectra.mgf -o similarities.txt`
**Explanation:** Computes similarity scores between spectra.

### With trained model
**Args:** `ms2deepscore -i spectra.mgf -m model.pt -o similarities.txt`
**Explanation:** Uses pre-trained model for predictions.

### Generate similarity matrix
**Args:** `ms2deepscore -i spectra.mgf -m -o matrix.txt`
**Explanation:** Generates pairwise similarity matrix.

### Batch processing
**Args:** `ms2deepscore -i mgf/ -o results/`
**Explanation:** Processes multiple spectrum files.

### Evaluate model
**Args:** `ms2deepscore evaluate -i test.mgf -m model.pt -o metrics.txt`
**Explanation:** Evaluates model performance.