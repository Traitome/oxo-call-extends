---
name: contrafold
category: containerization
description: Conditional training for RNA secondary structure prediction
tags: [contrafold, rna, secondary-structure, prediction, machine-learning]
author: oxo-call-community
source_url: "http://contra.stanford.edu/contrafold/"
---

## Concepts

- **Tool Overview**: ContraFold is a machine learning approach for RNA secondary structure prediction that uses conditional training to improve accuracy over traditional thermodynamic methods.
- **Core Function**: Predicts RNA secondary structures using probabilistic models trained on known structures.
- **Algorithm**: Uses conditional log-linear models (CLLMs) with discriminative training to learn structure parameters.
- **Input**: RNA sequences in FASTA format.
- **Output**: Predicted secondary structures in dot-bracket notation or other formats.
- **Application**: RNA structure prediction, non-coding RNA analysis, and structure-based function prediction.
- **Installation**: Install via bioconda: `conda install -c bioconda contrafold`

## Pitfalls

- **Training Data Bias**: Predictions reflect training dataset characteristics.
- **Pseudoknots**: Standard model does not predict pseudoknots.
- **Sequence Length**: Very long sequences may be computationally expensive.
- **Non-canonical Pairs**: May not accurately predict non-canonical base pairs.
- **Ionic Conditions**: Predictions assume standard ionic conditions.

## Examples

### Predict RNA secondary structure
**Args:** `contrafold predict input.fasta --output structure.dbn`
**Explanation:** Predicts secondary structure for RNA sequences.

### With partition function
**Args:** `contrafold partition input.fasta --output partition.txt`
**Explanation:** Calculates partition function and base pairing probabilities.

### Sample from ensemble
**Args:** `contrafold sample input.fasta --n 100 --output samples.dbn`
**Explanation:** Samples 100 structures from the Boltzmann ensemble.

### Display help
**Args:** `contrafold --help`
**Explanation:** Shows all available options and usage information.