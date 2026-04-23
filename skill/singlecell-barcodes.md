---
name: singlecell-barcodes
category: formatting
description: whitelisted singlecell barcodes and information regarding where molecular/sample/cellular barcodes are in each read, for various singlecell protocols
tags: [singlecell-barcodes, formatting, sam]
author: oxo-call-community
source_url: "https://github.com/roryk/singlecell-barcodes"
---

## Concepts

- **Tool Overview**: singlecell-barcodes (v0.2) - whitelisted singlecell barcodes and information regarding where molecular/sample/cellular barcodes are in each read, for various singlecell protocols
- **Core Function**: whitelisted singlecell barcodes and information regarding where molecular/sample/cellular barcodes are in each read, for various singlecell protocols
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda singlecell-barcodes`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `singlecell-barcodes -i <input_file> -o <output_file>`
**Explanation:** Run singlecell-barcodes with typical input and output options.
