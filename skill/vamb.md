---
name: vamb
category: bioinformatics
description: VAMB - Variational Autoencoder for Metagenomic Binning.
tags: [vamb, metagenomics, binning, machine-learning]
author: oxo-call-community
source_url: "https://github.com/RasmussenLab/vamb"
---

## Concepts

- **Tool Overview**: VAMB - A variational autoencoder for metagenomic binning.
- **Core Function**: Uses deep learning for metagenomic binning.
- **Input**: Metagenomic sequences, abundance profiles.
- **Output**: Binned contigs.
- **Installation**: Install via pip
- **Use Case**: Metagenomics, binning, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for training.
- **Training Time**: May be slow for large datasets.

## Examples

### Run VAMB binning
**Args:** `vamb --outdir bins/ --fasta contigs.fasta --rpkm abundances.tsv`
**Explanation:** Perform metagenomic binning with VAMB.

### With options
**Args:** `vamb --outdir bins/ --fasta contigs.fasta --rpkm abundances.tsv --cuda`
**Explanation:** Use GPU acceleration.
