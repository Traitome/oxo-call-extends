---
name: bakdrive
category: metagenomics
description: Bakdrive finds a minimum set of driver species from real metagenomic samples and simulates fecal microbial transplantation (FMT) process
tags: [bakdrive, metagenomics, SAM]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/bakdrive"
---

## Concepts

- **Tool Overview**: bakdrive (v1.0.4) - Bakdrive finds a minimum set of driver species from real metagenomic samples and simulates fecal microbial transplantation (FMT) process
- **Core Function**: Bakdrive finds a minimum set of driver species from real metagenomic samples and simulates fecal microbial transplantation (FMT) process
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda bakdrive`

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
