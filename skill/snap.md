---
name: snap
category: annotation
description: Semi-HMM-based Nucleic Acid Parser - a gene prediction tool.
tags: [snap, annotation, hmm]
author: oxo-call-community
source_url: "https://github.com/KorfLab/SNAP/blob/master/README.md"
---

## Concepts

- **Tool Overview**: snap (v2017_03_01) - Semi-HMM-based Nucleic Acid Parser - a gene prediction tool.
- **Core Function**: Semi-HMM-based Nucleic Acid Parser - a gene prediction tool.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snap`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snap -i <input.fasta> -o <output.gff>`
**Explanation:** Run snap with typical input and output options.
