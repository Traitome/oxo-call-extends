---
name: linearfold
category: rna
description: LinearFold - Linear-Time Prediction for RNA Secondary Structures
tags: [linearfold, rna, secondary-structure, prediction, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/LinearFold/LinearFold"
---

## Concepts

- **RNA Secondary Structure**: Prediction of RNA secondary structures
- **Linear-Time Algorithm**: Linear-time prediction algorithm
- **Energy Minimization**: Minimum free energy structure prediction
- **Base Pairing**: Prediction of base pairing interactions
- **Pseudoknots**: Supports pseudoknot prediction
- **Large RNAs**: Designed for large RNA sequences

## Pitfalls

- **Energy Model**: Energy parameters may not be accurate for all sequences
- **Pseudoknot Complexity**: Complex pseudoknots may be missed
- **Sequence Length**: Very long sequences may require significant resources
- **Parameter Tuning**: Requires careful parameter optimization
- **Output Format**: Multiple output formats available
- **Comparative Analysis**: May differ from other prediction tools

## Examples

### Predict RNA structure
**Args:** `linearfold -i rna.fasta -o structure.dot`
**Explanation:** Predicts RNA secondary structure from FASTA file.

### Energy minimization
**Args:** `linearfold -i rna.fasta -o structure.dot --energy`
**Explanation:** Outputs minimum free energy structure.

### Pseudoknot prediction
**Args:** `linearfold -i rna.fasta -o structure.dot --pseudoknot`
**Explanation:** Enables pseudoknot prediction.

### Multiple sequences
**Args:** `linearfold -i sequences.fasta -o structures/`
**Explanation:** Processes multiple RNA sequences.

### Dot bracket output
**Args:** `linearfold -i rna.fasta -o structure.txt --format dot`
**Explanation:** Outputs structure in dot-bracket notation.

### JSON output
**Args:** `linearfold -i rna.fasta -o structure.json --format json`
**Explanation:** Outputs structure in JSON format.