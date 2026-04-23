---
name: te-aid
category: annotation
description: Annotation helper tool for the manual curation of transposable element consensus sequences
tags: [te-aid, annotation]
author: oxo-call-community
source_url: "https://github.com/clemgoub/TE-Aid/tree/v{version}"
---

## Concepts

- **Tool Overview**: te-aid (v1.0.0) - Annotation helper tool for the manual curation of transposable element consensus sequences
- **Core Function**: Annotation helper tool for the manual curation of transposable element consensus sequences
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda te-aid`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `te-aid -i <input.fasta> -o <output.gff>`
**Explanation:** Run te-aid with typical input and output options.
