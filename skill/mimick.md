---
name: mimick
category: variant-calling
description: Simulate linked-read data
tags: [mimick, variant-calling]
author: oxo-call-community
source_url: "https://github.com/pdimens/mimick"
---

## Concepts

- **Tool Overview**: mimick v3.0.1 - Mimick, formerly known as XENIA from the VISOR project, can simulate all manner of available linked-read chemistries (10x, haplotagging, stlfr, tellseq). It allows you to simulate an arbitrary number of haplotypes, set overall coverage, molecule coverage, molecules per barcode, whether DNA is circular, etc..
- **Core Function**: Simulate linked-read data
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mimick`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
