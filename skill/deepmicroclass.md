---
name: deepmicroclass
category: metagenomics
description: DeepMicroClass, a deep learning based contig classification tool (CPU version).
tags: [deepmicroclass, metagenomics, classification, deep-learning, contig]
author: oxo-call-community
source_url: "https://github.com/chengsly/DeepMicroClass"
---

## Concepts

- **Tool Overview**: DeepMicroClass v1.0.3 - Deep learning tool for classifying metagenomic contigs by origin (prokaryote, eukaryote, virus, etc.).
- **Core Function**: Classifies metagenomic contigs into taxonomic categories using deep learning models.
- **Input/Output**: Expects FASTA contigs; outputs classification results per contig.
- **Installation**: `conda install -c bioconda deepmicroclass`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure FASTA format with adequate contig length for reliable classification.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deepmicroclass predict --input contigs.fa --output classifications.tsv`
**Explanation:** Classifies metagenomic contigs by their likely origin.
