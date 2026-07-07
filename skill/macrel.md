---
name: macrel
category: utility
description: A pipeline for AMP (antimicrobial peptide) prediction
tags: [macrel, utility, AMP, antimicrobial-peptides]
author: oxo-call-community
source_url: "https://github.com/BigDataBiology/macrel"
---

## Concepts

- **Tool Overview**: macrel v1.6.0 is a pipeline for predicting antimicrobial peptides (AMPs) from (meta)genomic sequences.
- **Core Function**: Identifies potential antimicrobial peptides using machine learning models.
- **AMP Prediction**: Uses trained models to classify sequences as AMPs or non-AMPs.
- **Input/Output**: Input: FASTA sequences; Output: Predicted AMPs with confidence scores.
- **Installation**: `conda install -c bioconda macrel`
- **Key Features**: Handles metagenomic data, provides confidence scores, supports batch processing.

## Pitfalls

- **Sequence Quality**: Low-quality sequences can affect prediction accuracy.
- **Model Limitations**: May not detect novel AMPs with unusual characteristics.
- **Memory Usage**: Processing large metagenomic datasets may require significant memory.
- **Computation Time**: Can be slow for very large datasets.
- **False Positives**: May produce false positive predictions requiring manual validation.
- **Training Data**: Model performance depends on training data diversity.

## Examples

### Predict AMPs from sequences
**Args:** `macrel predict -i sequences.fasta -o predictions.txt`
**Explanation:** Predicts antimicrobial peptides from input sequences.

### With custom model
**Args:** `macrel predict -i sequences.fasta -m custom_model.h5 -o predictions.txt`
**Explanation:** Uses custom-trained model for prediction.

### Threads
**Args:** `macrel predict -i sequences.fasta -t 8 -o predictions.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum confidence
**Args:** `macrel predict -i sequences.fasta -c 0.9 -o predictions.txt`
**Explanation:** Sets minimum confidence threshold to 90%.

### Output format
**Args:** `macrel predict -i sequences.fasta -f csv -o predictions.csv`
**Explanation:** Outputs results in CSV format.

### Help documentation
**Args:** `macrel --help`
**Explanation:** Displays all available commands and options.