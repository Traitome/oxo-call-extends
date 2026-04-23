---
name: demultiplex
category: utility
description: Demultiplex any number of FASTA or FASTQ files based on a list of barcodes.
tags: [demultiplex, utility, barcoding, fastq, fasta]
author: oxo-call-community
source_url: "https://github.com/jfjlaros/demultiplex"
---

## Concepts

- **Tool Overview**: demultiplex v1.2.2 - Tool for demultiplexing FASTA/FASTQ files based on barcode lists.
- **Core Function**: Splits sequencing reads into separate files based on barcode sequences.
- **Input/Output**: Expects FASTA/FASTQ files and barcode list; outputs demultiplexed read files per sample.
- **Installation**: `conda install -c bioconda demultiplex`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires barcode list matching read header or sequence positions.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `demultiplex --input reads.fq --barcodes barcodes.txt --output output_dir/`
**Explanation:** Demultiplexes reads based on barcode sequences.
