---
name: deepsig
category: annotation
description: Predictor of signal peptides in proteins based on deep learning.
tags: [deepsig, annotation, signal-peptide, deep-learning, protein]
author: oxo-call-community
source_url: "https://github.com/BolognaBiocomp/deepsig"
---

## Concepts

- **Tool Overview**: DeepSig v1.2.5 - Deep learning predictor of signal peptides in protein sequences.
- **Core Function**: Predicts signal peptides and their cleavage sites in protein sequences using convolutional neural networks.
- **Input/Output**: Expects protein FASTA files; outputs signal peptide predictions with cleavage site positions.
- **Installation**: `conda install -c bioconda deepsig`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure protein sequences in valid FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepsig -f proteins.fa -o predictions.tsv -k euk`
**Explanation:** Predicts signal peptides in eukaryotic protein sequences.
