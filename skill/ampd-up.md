---
name: ampd-up
category: annotation
description: De novo antimicrobial peptide sequence generation with recurrent neural networks
tags: [ampd-up, AMP, antimicrobial-peptides, RNN, deep-learning, peptide-design]
author: oxo-call-community
source_url: "https://github.com/BirolLab/AMPd-Up"
---

## Concepts

- **Tool Overview**: AMPd-Up is a deep learning tool that uses recurrent neural networks (RNN) for de novo antimicrobial peptide (AMP) sequence generation.
- **Core Function**: Generates novel AMP sequences by training on existing AMP datasets or using pre-trained models, enabling discovery of potential new antimicrobial peptides.
- **Input/Output**: Inputs: Training data (FASTA format), pre-trained models; Outputs: Generated peptide sequences in FASTA or TSV format.
- **Installation**: Available via Bioconda (`conda install -c bioconda ampd-up`) or from source.
- **Dependencies**: Python 3.6+, PyTorch 1.7.1, NumPy, Pandas, Biopython.

## Pitfalls

- **Python Version**: Requires Python 3.6; may have compatibility issues with newer versions.
- **Model Availability**: Pre-trained models need to be downloaded separately from Zenodo repository.
- **Training Data**: High-quality training data is essential for generating meaningful sequences.
- **GPU Acceleration**: Training large models may benefit from GPU acceleration for faster convergence.
- **Sequence Validation**: Generated sequences should be experimentally validated for antimicrobial activity.

## Examples

### Generate sequences with new models
**Args:** `AMPd-Up -n 100`
**Explanation:** Trains new RNN models and generates 100 novel AMP sequences.

### Generate sequences from pre-trained models
**Args:** `AMPd-Up -fm ../models/ -n 100`
**Explanation:** Samples 100 sequences from existing pre-trained models in the specified directory.

### Generate with custom training data
**Args:** `AMPd-Up -tr training_data.fasta -n 200`
**Explanation:** Trains RNN models on custom training data and generates 200 sequences.

### Save trained models
**Args:** `AMPd-Up -tr training_data.fasta -n 100 -sm my_model`
**Explanation:** Trains models, generates 100 sequences, and saves models with prefix "my_model".

### Specify output directory and format
**Args:** `AMPd-Up -n 50 -od results/ -of fasta`
**Explanation:** Generates 50 sequences and saves them in FASTA format in the results directory.

### Full workflow with training
**Args:** `AMPd-Up -tr APD3_ABP_20190320.fa -n 1000 -sm amp_models -od generated_peptides/ -of fasta`
**Explanation:** Trains on APD3 antibacterial peptide dataset, generates 1000 sequences, saves models, and outputs in FASTA format.