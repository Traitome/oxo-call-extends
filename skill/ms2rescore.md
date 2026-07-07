---
name: ms2rescore
category: utility
description: AI-assisted rescoring platform for peptide identifications from mass spectrometry.
tags: [ms2rescore, utility, proteomics]
author: oxo-call-community
source_url: "https://github.com/compomics/ms2rescore"
---

## Concepts

- **Tool Overview**: MS2Rescore v3.2.1 uses AI to improve peptide identification.
- **Core Function**: Rescores peptide identifications using machine learning.
- **Peptide ID**: Improves confidence of peptide assignments.
- **AI-powered**: Leverages deep learning for rescoring.
- **Proteomics**: Specialized for proteomics data analysis.
- **Input/Output**: Accepts search results; outputs rescored identifications.

## Pitfalls

- **Proteomics Specific**: Designed for mass spectrometry data.
- **Search Engine Output**: Requires output from search engines.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for rescoring.
- **Data Quality**: Results depend on initial search quality.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Rescore peptide identifications
**Args:** `ms2rescore -i search_results.mzid -o rescored.txt`
**Explanation:** Rescores peptide identifications.

### With machine learning model
**Args:** `ms2rescore -i search_results.mzid -m model.pt -o rescored.txt`
**Explanation:** Uses specific ML model for rescoring.

### Generate q-value report
**Args:** `ms2rescore -i search_results.mzid -q -o results.txt`
**Explanation:** Calculates q-values for identifications.

### Batch processing
**Args:** `ms2rescore -i mzid/ -o results/`
**Explanation:** Processes multiple search result files.

### Export for downstream analysis
**Args:** `ms2rescore -i search_results.mzid -e tsv -o results.tsv`
**Explanation:** Exports results in TSV format.