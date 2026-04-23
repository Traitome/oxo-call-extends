---
name: tiptoft
category: annotation
description: Predict plasmids from uncorrected long read data.
tags: [tiptoft, annotation]
author: oxo-call-community
source_url: "https://github.com/andrewjpage/tiptoft"
---

## Concepts

- **Tool Overview**: tiptoft (v1.0.2) - Predict plasmids from uncorrected long read data.
- **Core Function**: Predict plasmids from uncorrected long read data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tiptoft`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tiptoft -i <input.fasta> -o <output.gff>`
**Explanation:** Run tiptoft with typical input and output options.
