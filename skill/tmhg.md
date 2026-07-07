---
name: tmhg
category: analysis
description: TMHG - Transmembrane Helix prediction tool.
tags: [tmhg, transmembrane, helix, protein-structure, prediction, topology]
author: oxo-call-community
source_url: "https://github.com/compbio/tmhg"
---

## Concepts

- **Tool Overview**: TMHG (TransMembrane Helix predictor) - A tool for predicting transmembrane alpha-helices and their topology.
- **Core Function**: Identifies transmembrane helices, predicts their boundaries, and determines membrane topology.
- **Input**: Protein sequences (FASTA).
- **Output**: Transmembrane helix predictions, topology models, confidence scores.
- **Installation**: `pip install tmhg` or `conda install -c bioconda tmhg`
- **Use Case**: Membrane protein analysis, structural biology, drug discovery.

## Pitfalls

- **Alpha-helical Specific**: Only predicts alpha-helical membrane proteins.
- **Signal Peptides**: May confuse signal peptides with transmembrane helices.

## Examples

### Predict transmembrane helices
**Args:** `tmhg -i protein.fasta -o helix_prediction/`
**Explanation:** Predict transmembrane helices and topology for protein sequence.

### Detailed output
**Args:** `tmhg -i sequence.fasta --detailed -o detailed_results/`
**Explanation:** Generate detailed transmembrane helix prediction report.
