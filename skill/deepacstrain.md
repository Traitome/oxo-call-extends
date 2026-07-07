---
name: deepacstrain
category: utility
description: DeePaC-Strain - predicting pathogenic potentials of novel bacterial strains.
tags: [deepacstrain, utility, pathogen-prediction, bacterial-strains, deep-learning]
author: oxo-call-community
source_url: "https://rki_bioinformatics.gitlab.io/DeePaC/"
---

## Concepts

- **Tool Overview**: deepacstrain (v0.2.1+) is a deep learning tool for predicting the pathogenic potential of novel strains of known bacterial species. It analyzes genomic sequences to determine virulence potential.
- **Core Function**: Predicts whether a bacterial strain is likely to be pathogenic based on its genomic sequence, enabling rapid assessment of novel isolates.
- **Input/Output**: Input: Bacterial genome sequence (FASTA). Output: Pathogenicity probability score, virulence factor predictions, classification report.
- **Algorithm**: Uses deep neural networks trained on known pathogenic and non-pathogenic bacterial genomes to predict pathogenic potential.
- **Key Features**: Strain-level prediction, rapid assessment, supports multiple bacterial species, probability-based scoring, interpretable results.
- **Installation**: `conda install -c bioconda deepacstrain`

## Pitfalls

- **Training Data Bias**: Model performance depends on training data diversity.
- **Novel Species**: May not perform well on species not in training data.
- **Genome Completeness**: Requires complete or near-complete genome sequences.
- **Horizontal Transfer**: May miss horizontally acquired virulence factors.
- **Confidence Threshold**: Requires appropriate threshold setting for classification.

## Examples

### Predict pathogenic potential
**Args:** `deepacstrain -i genome.fasta -o prediction.txt`
**Explanation:** Predict pathogenic potential of a bacterial genome.

### Get detailed output
**Args:** `deepacstrain -i genome.fasta -o prediction.txt --detailed`
**Explanation:** Generate detailed prediction with feature importance.

### Batch processing
**Args:** `deepacstrain -i genomes/ -o predictions/`
**Explanation:** Process multiple genomes in batch mode.