---
name: seqfold
category: annotation
description: Predict the minimum free energy and structure of nucleic acids.
tags: [seqfold, annotation]
author: oxo-call-community
source_url: "https://github.com/Lattice-Automation/seqfold"
---

## Concepts

- **Tool Overview**: seqfold (v0.9.0) - Predict the minimum free energy and structure of nucleic acids.
- **Core Function**: Predict the minimum free energy and structure of nucleic acids.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqfold`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqfold -i <input.fasta> -o <output.gff>`
**Explanation:** Run seqfold with typical input and output options.
