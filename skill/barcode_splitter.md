---
name: barcode_splitter
category: utility
description: Split multiple fastq files by matching barcodes in one or more of the sequence files. Barcodes in the tab-delimited barcodes.txt file are matched against the beginning (or end) of the specified index read(s). By default, barcodes must match exactly, but --mistmatches can be set higher if desired. Compressed input is read (from all files) if the first input file name ends in .gz. Reading of compressed input can be forced with the gzipin option.
tags: [barcode_splitter, utility, FASTQ]
author: oxo-call-community
source_url: "https://bitbucket.org/princeton_genomics/barcode_splitter"
---

## Concepts

- **Tool Overview**: barcode_splitter (v0.18.6) - Split multiple fastq files by matching barcodes in one or more of the sequence files. Barcodes in the tab-delimited barcodes.txt file are matched against the beginning (or end) of the specified index read(s). By default, barcodes must match exactly, but --mistmatches can be set higher if desired. Compressed input is read (from all files) if the first input file name ends in .gz. Reading of compressed input can be forced with the gzipin option.
- **Core Function**: Split multiple fastq files by matching barcodes in one or more of the sequence files. Barcodes in the tab-delimited barcodes.txt file are matched against the beginning (or end) of the specified index read(s). By default, barcodes must match exactly, but --mistmatches can be set higher if desired. Compressed input is read (from all files) if the first input file name ends in .gz. Reading of compressed input can be forced with the gzipin option.
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda barcode_splitter`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `--input input_file --output output_file`
**Explanation:** Process input and generate output
