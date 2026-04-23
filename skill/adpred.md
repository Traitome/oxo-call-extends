---
name: adpred
category: annotation
description: Deep learning model for predicting acidic transcription activation domains in protein sequences
tags: [transcription, activation-domain, protein, deep-learning, prediction]
author: oxo-call-community
source_url: "https://github.com/FredHutch/adpred"
---

## Concepts

- **Tool Overview**: ADpred is a deep learning model that predicts acidic transcription activation domains (ADs) within protein sequences, identifying regions with high AD functional probability.
- **Core Function**: Scans protein sequences to identify potential transcription activation domains, outputting probability scores for each residue.
- **Input/Output**: Input: Protein sequences (FASTA or plain text). Output: AD probability scores and identified domain regions.
- **Machine Learning**: Uses trained neural network model based on experimental data from high-throughput AD screens.
- **Installation**: Install via bioconda: `conda install -c bioconda adpred`

## Pitfalls

- **Acidic ADs Only**: Model specifically predicts acidic activation domains - may not detect other AD types.
- **Sequence Length**: Very short or very long sequences may affect prediction accuracy.
- **Threshold Selection**: Choose appropriate probability threshold for domain calling based on application.
- **Model Limitations**: Predictions are based on training data - novel AD types may be missed.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for ADpred.

### Predict ADs from FASTA file
**Args:** `predict -i proteins.fasta -o predictions.tsv`
**Explanation:** Predicts activation domains for all sequences in the FASTA file.

### Predict with custom threshold
**Args:** `predict -i protein.fasta -o results.tsv --threshold 0.7`
**Explanation:** Uses 0.7 probability threshold for domain calling (higher stringency).

### Predict single sequence
**Args:** `predict -s "MKPQSTVNAL..." -o result.tsv`
**Explanation:** Predicts ADs for a single protein sequence provided directly on command line.

### Output with visualization
**Args:** `predict -i proteins.fasta -o results.tsv --plot`
**Explanation:** Generates probability plots for each predicted domain region.

### Batch process with summary
**Args:** `predict -i proteins.fasta -o results.tsv --summary summary.txt`
**Explanation:** Creates summary file with statistics on predicted domains across all proteins.

### Run saturation mutagenesis analysis
**Args:** `mutagenesis -i protein.fasta -d "50-100" -o mutagenesis.tsv`
**Explanation:** Performs in silico saturation mutagenesis on specified domain region to identify critical residues.
