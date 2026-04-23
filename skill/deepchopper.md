---
name: deepchopper
category: metagenomics
description: A Genomic Language Model for Chimera Artifact Detection in Nanopore Direct RNA Sequencing.
tags: [deepchopper, metagenomics, FASTQ]
author: oxo-call-community
source_url: "https://github.com/ylab-hi/DeepChopper"
---

## Concepts

- **Tool Overview**: deepchopper (v1.2.9) - A Genomic Language Model for Chimera Artifact Detection in Nanopore Direct RNA Sequencing.
- **Core Function**: DeepChopper is a genomic language model designed to identify artificial sequences. It provides functionality for encoding FASTQ files, making predictions, and chopping sequences.
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda deepchopper`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i contigs.fasta -o bins_dir`
**Explanation:** Perform metagenomic analysis
