---
name: dca
category: expression
description: Count autoencoder for scRNA-seq denoising
tags: [dca, expression]
author: oxo-call-community
source_url: "https://github.com/theislab/dca"
---

## Concepts

- **Tool Overview**: dca (v0.3.4) - Count autoencoder for scRNA-seq denoising
- **Core Function**: Count autoencoder for scRNA-seq denoising
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda dca`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
