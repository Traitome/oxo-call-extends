---
name: immunotype
category: immunology
description: Peptide-based HLA typing from immunopeptidomics data
tags: [immunotype, HLA-typing, immunopeptidomics, MHC]
author: oxo-call-community
source_url: "https://github.com/AG-Walz/immunotype"
---

## Concepts

- **Tool Overview**: immunotype (v1.0.2) is a machine learning tool for HLA class I allele prediction directly from immunopeptidomics mass spectrometry data.
- **Core Function**: Combines a graph neural network with a curated mono-allelic lookup table in an ensemble model to achieve 87.2% accuracy at protein-level resolution.
- **Input/Output**: Accepts peptide lists from mass spectrometry analysis. Outputs predicted HLA class I alleles with confidence scores.
- **No Separate Typing Needed**: Eliminates the need for separate HLA typing experiments by predicting alleles from immunopeptidomics data.
- **Multi-tissue Support**: Achieves high accuracy across diverse human tissues, making it suitable for various sample types.

## Pitfalls

- **Peptide Coverage**: Requires sufficient peptide coverage for accurate prediction; low-quality MS data may reduce performance.
- **Class I Focus**: Currently limited to HLA class I typing; does not support class II prediction.
- **Mass Spectrometry Dependencies**: Results depend on the quality and depth of the immunopeptidomics data input.
- **Allele Resolution**: Provides protein-level resolution; may not distinguish between closely related alleles.
- **Validation Required**: Predicted alleles should be validated with orthogonal methods for clinical applications.

## Examples

### Predict HLA alleles from peptide list
**Args:** `immunotype predict -i peptides.csv -o hla_predictions.tsv`
**Explanation:** Predicts HLA class I alleles from a CSV file containing identified peptides.

### Include confidence thresholds
**Args:** `immunotype predict -i peptides.csv -o results.tsv --min-confidence 0.8`
**Explanation:** Filters predictions to include only alleles with confidence score ≥ 0.8.

### Output detailed report
**Args:** `immunotype predict -i peptides.csv -o report.tsv --detailed`
**Explanation:** Generates a detailed report with allele frequencies and prediction probabilities.

### Batch processing multiple samples
**Args:** `immunotype batch -d sample_dir/ -o results/ --threads 4`
**Explanation:** Processes multiple peptide files in parallel using 4 threads.

### Train custom model
**Args:** `immunotype train -i training_data/ -o custom_model.pkl -e 50`
**Explanation:** Trains a custom model on provided training data for 50 epochs.

### Validate predictions
**Args:** `immunotype validate -i predictions.tsv -g gold_standard.tsv -o metrics.json`
**Explanation:** Validates predictions against a gold standard HLA typing and generates performance metrics.