---
name: centroid_rna_package
category: rna-analysis
description: Collection of RNA secondary structure prediction programs based on gamma-centroid estimator
tags: [centroid_rna_package, rna, secondary-structure, prediction, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/satoken/centroid-rna-package"
---

## Concepts

- **Tool Overview**: centroid_rna_package provides RNA secondary structure prediction programs based on the gamma-centroid estimator.
- **Core Function**: Predicts RNA secondary structures using probabilistic centroid estimation methods.
- **Algorithm**: Uses gamma-centroid estimator to find consensus structures from ensemble predictions.
- **Input**: RNA sequence in FASTA or plain text format.
- **Output**: Predicted RNA secondary structure in dot-bracket notation.
- **Application**: RNA structure analysis, non-coding RNA research, and RNA functional studies.
- **Installation**: Install via bioconda: `conda install -c bioconda centroid_rna_package`

## Pitfalls

- **Sequence Length**: May have limitations for very long RNA sequences.
- **Computational Time**: Structure prediction can be computationally intensive.
- **Energy Parameters**: Uses specific energy parameters that may need adjustment.
- **pseudoPKnots**: Does not handle pseudo-knots by default.

## Examples

### Predict RNA secondary structure
**Args:** `centroid_fold input.fasta output.structure`
**Explanation:** Predicts RNA secondary structure using centroid estimator.

### Calculate base pairing probabilities
**Args:** `centroid_prob input.fasta output.prob`
**Explanation:** Computes base pairing probabilities for each position.

### Predict with gamma parameter
**Args:** `centroid_fold -g 1.0 input.fasta output.structure`
**Explanation:** Uses gamma=1.0 for centroid estimation.

### Display help
**Args:** `centroid_fold --help`
**Explanation:** Shows all available options and usage information.