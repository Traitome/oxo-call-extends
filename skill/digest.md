---
name: digest
category: utility
description: In silico digestion of protein sequences.
tags: [digest, utility, proteomics, digestion]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: digest - In silico protein digestion tool for mass spectrometry applications.
- **Core Function**: Simulates enzymatic digestion of protein sequences to generate peptide lists.
- **Input/Output**: Expects protein FASTA files; outputs digested peptide sequences.
- **Installation**: `conda install -c bioconda digest`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires protein sequences in FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `digest --input proteins.fa --output peptides.fa`
**Explanation:** Performs in silico digestion of protein sequences.
