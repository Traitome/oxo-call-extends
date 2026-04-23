---
name: secapr
category: population-genomics
description: Process sequence-capture FASTQ files into alignments for phylogenetic analyses. Integrates allele phasing.
tags: [secapr, population-genomics, fastq]
author: oxo-call-community
source_url: "https://github.com/AntonelliLab/seqcap_processor"
---

## Concepts

- **Tool Overview**: secapr (v2.2.8) - Process sequence-capture FASTQ files into alignments for phylogenetic analyses. Integrates allele phasing.
- **Core Function**: Process sequence-capture FASTQ files into alignments for phylogenetic analyses. Integrates allele phasing.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda secapr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `secapr -i <input.vcf> -o <output_dir>`
**Explanation:** Run secapr with typical input and output options.
