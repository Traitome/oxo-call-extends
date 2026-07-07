---
name: mokapot
category: utility
description: Fast and flexible semi-supervised learning for peptide detection
tags: [mokapot, utility, proteomics]
author: oxo-call-community
source_url: "https://github.com/wfondrie/mokapot"
---

## Concepts

- **Tool Overview**: mokapot v0.10.0 uses semi-supervised learning for peptide detection.
- **Core Function**: Identifies peptides from mass spectrometry data using machine learning.
- **Semi-supervised Learning**: Combines labeled and unlabeled data for training.
- **Peptide Identification**: Improves peptide detection sensitivity.
- **Input/Output**: Accepts search engine results; outputs confident peptide identifications.
- **Proteomics**: Supports mass spectrometry-based proteomics workflows.

## Pitfalls

- **Proteomics Specific**: Designed for mass spectrometry data.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal performance.
- **Data Quality**: Results depend on MS data quality.
- **Search Engine Dependence**: Requires search engine results as input.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Run peptide detection
**Args:** `mokapot -i search_results.txt -o confident_peptides.txt`
**Explanation:** Identifies confident peptides using semi-supervised learning.

### With multiple inputs
**Args:** `mokapot -i search1.txt search2.txt -o confident_peptides.txt`
**Explanation:** Combines results from multiple searches.

### Custom model
**Args:** `mokapot -i search_results.txt -m model.pkl -o confident_peptides.txt`
**Explanation:** Uses pre-trained model for prediction.

### Verbose output
**Args:** `mokapot -i search_results.txt -v -o confident_peptides.txt`
**Explanation:** Shows detailed classification results.

### Batch processing
**Args:** `mokapot -i searches/ -o results/`
**Explanation:** Processes multiple search result files.