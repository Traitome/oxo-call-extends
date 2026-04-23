---
name: deepmod
category: epigenomics
description: A deep-learning method for DNA modification (5mC and 6mA) prediction.
tags: [deepmod, epigenomics, methylation, deep-learning, nanopore]
author: oxo-call-community
source_url: "https://github.com/WGLab/DeepMod"
---

## Concepts

- **Tool Overview**: DeepMod v0.1.3 - Deep learning method for detecting DNA modifications (5mC and 6mA) from Nanopore sequencing data.
- **Core Function**: Predicts DNA methylation states (5mC, 6mA) from Oxford Nanopore signal data using recurrent neural networks.
- **Input/Output**: Expects Nanopore FAST5/FASTQ and reference genome; outputs methylation calls.
- **Installation**: `conda install -c bioconda deepmod`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Nanopore signal data and a reference genome for accurate predictions.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepmod detect --fastq reads.fq --reference ref.fa --output methylation/`
**Explanation:** Detects DNA methylation from Nanopore reads against a reference.
