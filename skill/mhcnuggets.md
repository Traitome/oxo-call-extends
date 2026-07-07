---
name: mhcnuggets
category: variant-calling
description: "MHCnuggets: Neoantigen peptide MHC binding prediction for class I and II"
tags: [mhcnuggets, variant-calling, immunology]
author: oxo-call-community
source_url: "http://karchinlab.org/apps/mhcnuggets.html"
---
## Concepts

- **Tool Overview**: MHCnuggets v2.4.1 predicts neoantigen peptide-MHC binding for class I and II.
- **Core Function**: Predicts peptide-MHC binding for neoantigen identification.
- **Neoantigen Prediction**: Identifies potential neoantigens from somatic mutations.
- **Deep Learning**: Uses deep learning models for binding prediction.
- **Input/Output**: Accepts peptide sequences; outputs binding predictions.
- **Cancer Immunology**: Used in cancer immunotherapy research.

## Pitfalls

- **Deep Learning Dependencies**: Requires TensorFlow/Keras.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal predictions.
- **Data Quality**: Prediction accuracy depends on input data quality.
- **Model Training**: Requires model training on large datasets.

## Examples

### Predict MHC binding
**Args:** `mhcnuggets predict -i peptides.txt -o predictions.txt`
**Explanation:** Predicts peptide-MHC binding affinity.

### MHC class I prediction
**Args:** `mhcnuggets predict -i peptides.txt -o predictions.txt -c I`
**Explanation:** Predicts MHC class I binding.

### MHC class II prediction
**Args:** `mhcnuggets predict -i peptides.txt -o predictions.txt -c II`
**Explanation:** Predicts MHC class II binding.

### With specific allele
**Args:** `mhcnuggets predict -i peptides.txt -o predictions.txt -a HLA-A*02:01`
**Explanation:** Predicts binding to specific MHC allele.

### Batch processing
**Args:** `mhcnuggets predict -i peptides/ -o predictions/`
**Explanation:** Processes multiple peptide files in batch mode.