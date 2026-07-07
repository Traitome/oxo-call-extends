---
name: deepsig
category: annotation
description: DeepSig - deep learning predictor of signal peptides in proteins.
tags: [deepsig, annotation, signal-peptide, deep-learning, protein]
author: oxo-call-community
source_url: "https://github.com/BolognaBiocomp/deepsig"
---

## Concepts

- **Tool Overview**: deepsig (v1.2.5+) is a deep learning-based predictor of signal peptides in protein sequences. It identifies signal peptides and their cleavage sites with high accuracy.
- **Core Function**: Predicts signal peptides and their cleavage sites in protein sequences using convolutional neural networks, enabling identification of secreted proteins.
- **Input/Output**: Input: Protein FASTA files. Output: Signal peptide predictions, cleavage site positions, confidence scores.
- **Algorithm**: Uses convolutional neural networks to learn patterns associated with signal peptide sequences and cleavage sites.
- **Key Features**: High accuracy, supports multiple organisms (eukaryotic, prokaryotic, archaeal), cleavage site prediction, batch processing, confidence scoring.
- **Installation**: `conda install -c bioconda deepsig`

## Pitfalls

- **Sequence Quality**: Requires good quality protein sequences.
- **Organism Specificity**: Must select appropriate organism type.
- **Short Sequences**: May struggle with very short sequences.
- **Signal Peptide Diversity**: May miss unusual signal peptide types.
- **False Positives**: May produce false positive predictions.

## Examples

### Predict signal peptides in eukaryotes
**Args:** `deepsig -f proteins.fa -o predictions.tsv -k euk`
**Explanation:** Predicts signal peptides in eukaryotic protein sequences.

### For prokaryotes
**Args:** `deepsig -f proteins.fa -o predictions.tsv -k pro`
**Explanation:** Predicts signal peptides in prokaryotic protein sequences.

### With detailed output
**Args:** `deepsig -f proteins.fa -o predictions.tsv -k euk -d`
**Explanation:** Generate detailed predictions with additional information.