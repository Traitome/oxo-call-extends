---
name: thapbi-pict
category: metagenomics
description: THAPBI Phytophthora ITS1 Classifier Tool (PICT).
tags: [thapbi-pict, metagenomics]
author: oxo-call-community
source_url: "https://thapbi-pict.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: thapbi-pict (v1.0.22) - THAPBI Phytophthora ITS1 Classifier Tool (PICT).
- **Core Function**: THAPBI Phytophthora ITS1 Classifier Tool (PICT).
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda thapbi-pict`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `thapbi-pict -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run thapbi-pict with typical input and output options.
