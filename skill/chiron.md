---
name: chiron
category: basecalling
description: Deep neural network basecaller for nanopore sequencing
tags: [chiron, nanopore, basecalling, deep-learning, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/haotianteng/chiron"
---

## Concepts

- **Tool Overview**: Chiron is a deep neural network-based basecaller for Oxford Nanopore sequencing data.
- **Core Function**: Converts raw nanopore signal data into nucleotide sequences using deep learning models.
- **Algorithm**: Uses convolutional neural networks (CNNs) and recurrent neural networks (RNNs) for accurate basecalling.
- **Input**: Raw nanopore signal files (FAST5 format).
- **Output**: Basecalled FASTQ sequences with quality scores.
- **Application**: Nanopore sequencing data processing and basecalling.
- **Installation**: Install via bioconda: `conda install -c bioconda chiron`

## Pitfalls

- **GPU Requirements**: Benefits from GPU acceleration; may be slow on CPU.
- **Model Selection**: Different models available for different accuracy/speed tradeoffs.
- **Signal Quality**: Basecalling accuracy depends on raw signal quality.
- **Memory Usage**: May require significant memory for large datasets.
- **Model Updates**: Newer models may improve accuracy over older versions.

## Examples

### Basecall FAST5 files
**Args:** `chiron call -i reads.fast5 -o output/ -m model`
**Explanation:** Basecalls raw nanopore signal files.

### With GPU acceleration
**Args:** `chiron call -i reads.fast5 -o output/ --gpu`
**Explanation:** Uses GPU for faster basecalling.

### Train custom model
**Args:** `chiron train -d training_data/ -o model/ -e 10`
**Explanation:** Trains a custom basecalling model.

### Display help
**Args:** `chiron --help`
**Explanation:** Shows all available options and usage information.