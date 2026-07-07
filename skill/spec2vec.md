---
name: spec2vec
category: metabolomics
description: Spec2Vec - Word2Vec based similarity measure for mass spectrometry data
tags: [spec2vec, metabolomics, mass-spectrometry, similarity, word2vec]
author: oxo-call-community
source_url: "https://spec2vec.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: spec2vec (v0.9.1) - A mass spectrometry similarity tool
- **Core Function**: Computes similarity using Word2Vec on MS data
- **Input/Output**: Accepts MS spectra; outputs similarity scores
- **Algorithm**: Word2Vec-based similarity measurement
- **Installation**: `conda install -c bioconda spec2vec`
- **Key Features**: MS similarity, Word2Vec, metabolomics analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted MS spectra
- **Spectra Quality**: Spectra quality affects similarity accuracy
- **Model Training**: Model training parameters affect results
- **Memory Usage**: Large spectral datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Similarity Threshold**: Threshold affects similarity classification

## Examples

### Display help
**Args:** `spec2vec --help`
**Explanation:** Shows available options and usage information.

### Basic similarity computation
**Args:** `spec2vec -i spectra.mgf -o similarity.tsv`
**Explanation:** Compute similarity between spectra.

### Train model
**Args:** `spec2vec -i spectra.mgf --train -o model.pkl`
**Explanation:** Train Word2Vec model on spectra.

### Load model
**Args:** `spec2vec -i spectra.mgf -m model.pkl -o similarity.tsv`
**Explanation:** Use pre-trained model for similarity.

### With similarity threshold
**Args:** `spec2vec -i spectra.mgf -o similarity.tsv --threshold 0.8`
**Explanation:** Set similarity threshold.

### Output detailed results
**Args:** `spec2vec -i spectra.mgf -o similarity.tsv --detailed`
**Explanation:** Output detailed similarity information.

### Output statistics
**Args:** `spec2vec -i spectra.mgf -o similarity.tsv --stats`
**Explanation:** Output similarity statistics.

### Generate report
**Args:** `spec2vec -i spectra.mgf -o similarity.tsv --report`
**Explanation:** Generate similarity report.

### With threads
**Args:** `spec2vec -i spectra.mgf -o similarity.tsv -p 8`
**Explanation:** Use multiple threads for computation.