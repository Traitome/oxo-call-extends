---
name: nanonet
category: utility
description: NanoNet - Recurrent neural network basecalling for Oxford Nanopore data
tags: [nanonet, utility, nanopore, basecalling, rnn, neural-network]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/nanonet"
---

## Concepts

- **Tool Overview**: NanoNet v2.0.0 is a recurrent neural network (RNN) based basecaller for Oxford Nanopore MinION sequencing data. It converts raw signal to nucleotide sequences.
- **Core Function**: Basecalls raw Nanopore signal data using deep learning models. Can also perform modified base detection during basecalling.
- **Algorithm**: Uses bidirectional LSTM (Long Short-Term Memory) networks to model signal-to-base transitions. Supports various neural network architectures.
- **Input Format**: Requires FAST5 files containing raw signal data from Nanopore sequencing runs.
- **Output**: Produces FASTQ files with base-called sequences and quality scores. Can also output modification probabilities.
- **Use Case**: Basecalling Nanopore sequencing data, research on neural network basecalling, and modified base detection during sequencing.

## Pitfalls

- **FAST5 Format**: Requires proper FAST5 file format. Mixed old/new formats may cause issues.
- **Model Compatibility**: Different sequencing kits require different models. Use appropriate model for your data.
- **GPU Acceleration**: Neural network basecalling requires GPU for reasonable performance. CPU-only mode is very slow.
- **Model Updates**: Models are periodically updated. Use latest models for best accuracy.
- **Quality Scores**: Basecall quality scores may need recalibration for specific use cases.
- **Deprecated**: Note that ONT's official Guppy basecaller is now more commonly used than NanoNet.

## Examples

### Basic basecalling
**Args:** `-i fast5_dir -o output.fastq`
**Explanation:** Basecalls FAST5 files using default RNN model.

### Specify model
**Args:** `-i fast5_dir -o output.fastq -m r941_min_high_g360`
**Explanation:** Uses specific model for R9.4.1 flow cells with high accuracy.

### Include modifications
**Args:** `-i fast5_dir -o output.fastq --modified_bases`
**Explanation:** Detects and outputs modified base probabilities.

### Use GPU
**Args:** `-i fast5_dir -o output.fastq --gpu`
**Explanation:** Uses GPU for accelerated basecalling.

### Display help
**Args:** `nanonet --help`
**Explanation:** Shows all available options for basecalling.
