---
name: deepnog
category: annotation
description: Deep learning tool for protein orthologous group assignment.
tags: [deepnog, annotation, orthologs, deep-learning, eggNOG]
author: oxo-call-community
source_url: "https://github.com/univieCUBE/deepnog"
---

## Concepts

- **Tool Overview**: deepNOG v1.2.4 - Deep learning tool for fast protein orthologous group assignment using the eggNOG database.
- **Core Function**: Assigns protein sequences to orthologous groups in eggNOG using deep neural networks, faster than traditional HMM approaches.
- **Input/Output**: Expects protein FASTA files; outputs orthologous group assignments.
- **Installation**: `conda install -c bioconda deepnog`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure protein sequences in valid FASTA format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepnog classify --input proteins.fa --output assignments.tsv`
**Explanation:** Assigns protein sequences to eggNOG orthologous groups.
