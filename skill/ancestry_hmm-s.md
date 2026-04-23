---
name: ancestry_hmm-s
category: expression
description: Inferring adaptive introgression from genomic data using hidden Markov models
tags: [ancestry_hmm-s, expression]
author: oxo-call-community
source_url: "https://github.com/jesvedberg/Ancestry_HMM-S"
---

## Concepts

- **Tool Overview**: ancestry_hmm-s (v0.9.0.2) - Inferring adaptive introgression from genomic data using hidden Markov models
- **Core Function**: Ancestry_HMM-S is a program designed to infer adaptive introgression from genomic data. It can both identify loci that has increased in frequency due to selection and quantify the strength of selectio...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ancestry_hmm-s`

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
