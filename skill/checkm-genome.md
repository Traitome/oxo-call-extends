---
name: checkm-genome
category: qc
description: Assess the quality of microbial genomes recovered from isolates, single cells, and metagenomes.
tags: [checkm-genome, qc]
author: oxo-call-community
source_url: "https://ecogenomics.github.io/CheckM"
---

## Concepts

- **Tool Overview**: checkm-genome (v1.2.5) - Assess the quality of microbial genomes recovered from isolates, single cells, and metagenomes.
- **Core Function**: Assess the quality of microbial genomes recovered from isolates, single cells, and metagenomes.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda checkm-genome`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
