---
name: codan
category: expression
description: CDS prediction in eukaryotic transcripts
tags: [codan, cds-prediction, gene-prediction, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/pedronachtigall/CodAn"
---

## Concepts

- **Tool Overview**: CodAn is a tool for predicting coding sequences (CDS) in eukaryotic transcripts, identifying potential protein-coding regions.
- **Core Function**: Predicts coding sequences within eukaryotic transcript sequences using machine learning models.
- **Algorithm**: Uses random forest classifiers trained on sequence features to identify CDS regions.
- **Input**: Transcript sequences in FASTA format.
- **Output**: Predicted CDS regions with coordinates and confidence scores.
- **Application**: Gene prediction, transcriptome analysis, and genome annotation.
- **Installation**: Install via bioconda: `conda install -c bioconda codan`

## Pitfalls

- **Training Data**: Performance depends on training data characteristics.
- **Species Specificity**: Models may be species-specific.
- **Alternative Splicing**: May not handle complex alternative splicing well.
- **Sequence Quality**: Requires high-quality transcript sequences.
- **Model Parameters**: May require tuning for specific datasets.

## Examples

### Predict CDS in transcripts
**Args:** `codan -i transcripts.fasta -o cds_predictions.gff`
**Explanation:** Predicts CDS regions in transcript sequences.

### With custom model
**Args:** `codan -i transcripts.fasta -m model.pkl -o cds_predictions.gff`
**Explanation:** Uses custom-trained model for prediction.

### Output FASTA format
**Args:** `codan -i transcripts.fasta -f fasta -o cds_sequences.fasta`
**Explanation:** Outputs predicted CDS sequences in FASTA format.

### Display help
**Args:** `codan --help`
**Explanation:** Shows all available options and usage information.