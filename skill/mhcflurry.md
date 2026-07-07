---
name: mhcflurry
category: utility
description: MHC Binding Predictor
tags: [mhcflurry, utility, immunology]
author: oxo-call-community
source_url: "https://github.com/openvax/mhcflurry"
---

## Concepts

- **Tool Overview**: MHCflurry v2.2.0 is an MHC binding predictor for peptide-MHC interactions.
- **Core Function**: Predicts peptide-MHC binding affinity.
- **MHC Class I/II**: Supports both MHC class I and class II predictions.
- **Machine Learning**: Uses machine learning models for prediction.
- **Input/Output**: Accepts peptide sequences; outputs binding predictions.
- **Immunoinformatics**: Used in vaccine design and immunogenomics.

## Pitfalls

- **Model Dependencies**: Requires trained machine learning models.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal predictions.
- **Data Quality**: Prediction accuracy depends on input data quality.
- **MHC Specificity**: Models are MHC allele-specific.

## Examples

### Predict MHC binding
**Args:** `mhcflurry predict -i peptides.txt -o predictions.txt`
**Explanation:** Predicts peptide-MHC binding affinity.

### With specific MHC allele
**Args:** `mhcflurry predict -i peptides.txt -o predictions.txt -a HLA-A*02:01`
**Explanation:** Predicts binding to specific MHC allele.

### MHC class II prediction
**Args:** `mhcflurry predict -i peptides.txt -o predictions.txt -c II`
**Explanation:** Predicts MHC class II binding.

### Batch processing
**Args:** `mhcflurry predict -i peptides/ -o predictions/`
**Explanation:** Processes multiple peptide files in batch mode.

### Generate binding scores
**Args:** `mhcflurry score -i peptides.txt -o scores.txt`
**Explanation:** Generates binding affinity scores.