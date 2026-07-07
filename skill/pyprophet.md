---
name: pyprophet
category: utility
description: PyProphet performs semi-supervised learning and scoring of OpenSWATH mass spectrometry results.
tags: [pyprophet, utility, mass-spectrometry, openswath]
author: oxo-call-community
source_url: "https://openswath.org/en/latest"
---

## Concepts

- **Tool Overview**: pyprophet scores OpenSWATH results.
- **Core Function**: Peak scoring.
- **Algorithm**: Uses machine learning.
- **Input Format**: Accepts OpenSWATH results.
- **Output**: Produces scored peaks.
- **Use Case**: Proteomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Training Data**: Affects model.
- **Feature Selection**: Affects scoring.
- **Runtime**: Scoring may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyprophet --help`
**Explanation:** Shows available options and usage instructions.

### Score peaks
**Args:** `pyprophet score -i openswath_results.tsv -o scored.tsv`
**Explanation:** Scores OpenSWATH peaks.

### With parameters
**Args:** `pyprophet score -i openswath_results.tsv -p params.yaml -o scored.tsv`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyprophet -v score -i openswath_results.tsv -o scored.tsv`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyprophet -t 4 score -i openswath_results.tsv -o scored.tsv`
**Explanation:** Uses 4 threads for parallel processing.

### Train model
**Args:** `pyprophet train -i training_data.tsv -o model.pkl`
**Explanation:** Trains scoring model.

### Generate report
**Args:** `pyprophet score -i openswath_results.tsv -o scored.tsv --report report.html`
**Explanation:** Generates HTML report.