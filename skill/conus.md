---
name: conus
category: containerization
description: SCFG-based RNA secondary structure analysis
tags: [conus, rna, secondary-structure, scfg, stochastic-grammar]
author: oxo-call-community
source_url: "http://eddylab.org/software/conus/"
---

## Concepts

- **Tool Overview**: CONUS is an implementation of simple stochastic context-free grammars (SCFGs) for RNA secondary structure analysis, designed to explore different SCFG designs for predicting RNA structures.
- **Core Function**: Uses probabilistic context-free grammars to model and predict RNA secondary structures from single sequences.
- **Algorithm**: Implements SCFG parsing with inside-outside algorithm for structure prediction and parameter estimation.
- **Input**: RNA sequences in FASTA format.
- **Output**: Predicted secondary structures in dot-bracket notation.
- **Application**: RNA structure prediction research, algorithm comparison, and grammar design exploration.
- **Installation**: Install via bioconda: `conda install -c bioconda conus`

## Pitfalls

- **Model Complexity**: Grammar design significantly affects prediction accuracy.
- **Pseudoknots**: Standard SCFGs cannot model pseudoknots.
- **Training Data**: Performance depends on training set composition.
- **Sequence Length**: Longer sequences increase computational complexity.
- **Parameter Estimation**: Requires sufficient training data for reliable parameters.

## Examples

### Predict RNA structure
**Args:** `conus -i input.fasta -o structure.dbn`
**Explanation:** Predicts RNA secondary structure using SCFG.

### Train custom grammar
**Args:** `conus -train training_structures.dbn -o grammar.cfg`
**Explanation:** Trains SCFG parameters from known structures.

### Compare grammars
**Args:** `conus -i input.fasta -g grammar1.cfg grammar2.cfg -o comparison.txt`
**Explanation:** Compares predictions from different grammar configurations.

### Display help
**Args:** `conus --help`
**Explanation:** Shows all available options and usage information.