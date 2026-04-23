---
name: smeg
category: metagenomics
description: Strain-level Metagenomic Estimation of Growth rate (SMEG) measures growth rates of microbial strains from complex metagenomic dataset
tags: [smeg, metagenomics]
author: oxo-call-community
source_url: "https://github.com/ohlab/SMEG"
---

## Concepts

- **Tool Overview**: smeg (v1.1.5) - Strain-level Metagenomic Estimation of Growth rate (SMEG) measures growth rates of microbial strains from complex metagenomic dataset
- **Core Function**: Strain-level Metagenomic Estimation of Growth rate (SMEG) measures growth rates of microbial strains from complex metagenomic dataset
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smeg`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smeg -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run smeg with typical input and output options.
