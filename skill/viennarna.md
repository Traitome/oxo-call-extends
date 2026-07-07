---
name: viennarna
category: bioinformatics
description: ViennaRNA - RNA secondary structure prediction.
tags: [viennarna, rna-structure, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/ViennaRNA/ViennaRNA"
---

## Concepts

- **Tool Overview**: ViennaRNA - RNA secondary structure analysis.
- **Core Function**: Predicts RNA secondary structures.
- **Input**: RNA sequence.
- **Output**: Structure predictions.
- **Installation**: Install via conda or source
- **Use Case**: RNA analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for long sequences.
- **Accuracy**: Predictions are probabilistic.

## Examples

### Predict structure
**Args:** `RNAfold < input.fasta > structure.txt`
**Explanation:** Predict RNA structure.

### With options
**Args:** `RNAfold -p < input.fasta > structure.txt`
**Explanation:** Calculate base pairing probabilities.
