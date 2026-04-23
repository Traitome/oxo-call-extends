---
name: demultiplexer
category: utility
description: Python tool to demultiplex Illumina reads tagged with the leeselab tagging scheme.
tags: [demultiplexer, utility, demultiplexing, illumina]
author: oxo-call-community
source_url: "https://github.com/DominikBuchner/demultiplexer"
---

## Concepts

- **Tool Overview**: demultiplexer v1.2.1 - Python tool for demultiplexing Illumina reads using the LeeseLab tagging scheme.
- **Core Function**: Separates multiplexed Illumina reads based on tagging barcodes.
- **Input/Output**: Expects FASTQ files; outputs demultiplexed FASTQ files per sample.
- **Installation**: `conda install -c bioconda demultiplexer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Illumina FASTQ files with appropriate tagging scheme.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `demultiplexer --input R1.fq R2.fq --output output_dir/`
**Explanation:** Demultiplexes paired-end Illumina reads.
