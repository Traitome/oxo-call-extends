---
name: linearpartition
category: rna
description: LinearPartition - Linear-Time Approximation of RNA Folding Partition Function
tags: [linearpartition, rna, partition-function, base-pairing, probability, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/LinearFold/LinearPartition"
---

## Concepts

- **Partition Function**: Calculates RNA folding partition function
- **Base Pairing Probabilities**: Computes base pairing probabilities
- **Linear-Time Algorithm**: Linear-time approximation algorithm
- **Free Energy**: Estimates free energy of RNA structures
- **Ensemble Prediction**: Predicts ensemble of RNA structures
- **RNA Thermodynamics**: RNA thermodynamic modeling

## Pitfalls

- **Approximation Error**: Linear-time approximation may introduce errors
- **Energy Parameters**: Energy parameters may affect accuracy
- **Sequence Length**: Very long sequences may require significant resources
- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Comparison**: Results may differ from exact methods

## Examples

### Calculate partition function
**Args:** `linearpartition -i rna.fasta -o partition.txt`
**Explanation:** Calculates RNA folding partition function.

### Base pairing probabilities
**Args:** `linearpartition -i rna.fasta -o probabilities.txt --prob`
**Explanation:** Computes base pairing probabilities.

### Free energy
**Args:** `linearpartition -i rna.fasta -o energy.txt --energy`
**Explanation:** Estimates free energy of RNA structure.

### Ensemble diversity
**Args:** `linearpartition -i rna.fasta -o ensemble.txt --ensemble`
**Explanation:** Outputs ensemble diversity measures.

### Multiple sequences
**Args:** `linearpartition -i sequences.fasta -o results/`
**Explanation:** Processes multiple RNA sequences.

### JSON output
**Args:** `linearpartition -i rna.fasta -o results.json --format json`
**Explanation:** Outputs results in JSON format.