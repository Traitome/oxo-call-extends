---
name: demultiplexer2
category: utility
description: A python command line interface to demultiplex Illumina reads.
tags: [demultiplexer2, utility, demultiplexing, illumina]
author: oxo-call-community
source_url: "https://github.com/DominikBuchner/demultiplexer2"
---

## Concepts

- **Tool Overview**: demultiplexer2 v1.1.6 - Python CLI for demultiplexing Illumina reads.
- **Core Function**: Separates multiplexed Illumina sequencing reads by sample barcodes.
- **Input/Output**: Expects FASTQ files; outputs demultiplexed FASTQ files per sample.
- **Installation**: `conda install -c bioconda demultiplexer2`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Illumina FASTQ files with sample barcodes.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `demultiplexer2 --input R1.fq R2.fq --barcodes barcodes.tsv --output output_dir/`
**Explanation:** Demultiplexes paired-end Illumina reads by barcodes.
