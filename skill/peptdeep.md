---
name: peptdeep
category: expression
description: PeptDeep provides deep learning models for proteomics.
tags: [peptdeep, expression, deep-learning, proteomics]
author: oxo-call-community
source_url: "https://github.com/MannLabs/alphapeptdeep"
---

## Concepts

- **Tool Overview**: PeptDeep predicts peptide properties.
- **Core Function**: Uses deep learning for proteomics.
- **Algorithm**: Uses AlphaX deep learning framework.
- **Input Format**: Accepts protein sequence files.
- **Output**: Produces predicted spectral libraries.
- **Use Case**: Proteomics, spectral library generation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large protein sets require memory.
- **Model Accuracy**: Predictions may have limitations.
- **Training Data**: Requires proper training data.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peptdeep --help`
**Explanation:** Shows available options and usage instructions.

### Predict spectra
**Args:** `peptdeep -i proteins.fasta -o spectral_library.msp`
**Explanation:** Predicts peptide spectral library.

### With models
**Args:** `peptdeep -i proteins.fasta -m models/ -o spectral_library.msp`
**Explanation:** Uses custom deep learning models.

### Verbose mode
**Args:** `peptdeep -v -i proteins.fasta -o spectral_library.msp`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peptdeep -t 4 -i proteins.fasta -o spectral_library.msp`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peptdeep -i proteins.fasta -o spectral_library.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peptdeep -i proteins.fasta -o spectral_library.msp --report report.html`
**Explanation:** Generates HTML report.