---
name: deepmased
category: qc
description: Deep learning for Metagenome Assembly Error Detection.
tags: [deepmased, qc, metagenomics, deep-learning, assembly]
author: oxo-call-community
source_url: "https://github.com/leylabmpi/DeepMAsED"
---

## Concepts

- **Tool Overview**: DeepMAsED v0.3.1 - Deep learning tool for detecting errors in metagenome assemblies.
- **Core Function**: Uses deep learning to identify misassembled contigs and assembly errors in metagenomic data.
- **Input/Output**: Expects assembled contigs (FASTA) and read mapping data; outputs error predictions per contig.
- **Installation**: `conda install -c bioconda deepmased`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires both assembly and read alignment data for accurate predictions.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepmased predict --assembly contigs.fa --bam alignment.bam --output results/`
**Explanation:** Predicts assembly errors from contigs and read mappings.
