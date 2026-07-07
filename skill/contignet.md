---
name: contignet
category: assembly
description: Deep learning-based phage-host interaction prediction
tags: [contignet, phage-host, deep-learning, interaction-prediction, metagenomics]
author: oxo-call-community
source_url: "https://github.com/tianqitang1/ContigNet"
---

## Concepts

- **Tool Overview**: ContigNet is a deep learning-based tool for predicting phage-host interactions from metagenomic contigs, enabling identification of bacteriophage hosts without cultivation.
- **Core Function**: Uses neural networks to predict which bacterial hosts are infected by specific phages based on sequence features.
- **Algorithm**: Implements convolutional neural networks (CNNs) to learn sequence patterns associated with phage-host relationships.
- **Input**: Phage and bacterial contig sequences in FASTA format.
- **Output**: Predicted phage-host interaction pairs with confidence scores.
- **Application**: Metagenomic analysis, phage therapy research, and microbial ecology studies.
- **Installation**: Install via bioconda: `conda install -c bioconda contignet`

## Pitfalls

- **Training Data Bias**: Predictions limited by training dataset diversity.
- **Sequence Length**: Short contigs may produce unreliable predictions.
- **Novel Phages**: May not accurately predict interactions for novel phage families.
- **Host Range**: May miss broad-host-range phage interactions.
- **Computational Resources**: Deep learning models require significant GPU resources.

## Examples

### Predict phage-host interactions
**Args:** `contignet predict -i phage_contigs.fasta -b bacterial_contigs.fasta -o interactions.txt`
**Explanation:** Predicts phage-host interactions from contig sequences.

### With trained model
**Args:** `contignet predict -i phage_contigs.fasta -b bacterial_contigs.fasta -m model.h5 -o interactions.txt`
**Explanation:** Uses custom trained model for prediction.

### Set confidence threshold
**Args:** `contignet predict -i phage_contigs.fasta -b bacterial_contigs.fasta -t 0.8 -o interactions.txt`
**Explanation:** Sets 80% confidence threshold for interaction predictions.

### Display help
**Args:** `contignet --help`
**Explanation:** Shows all available options and usage information.