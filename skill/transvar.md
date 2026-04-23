---
name: transvar
category: variant-calling
description: Transcript-based variant annotator.
tags: [transvar, variant-calling]
author: oxo-call-community
source_url: "https://transvar.readthedocs.io"
---

## Concepts

- **Tool Overview**: transvar (v2.5.10.20211024) - TransVar is a multi-way annotator for genetic elements and genetic variations. It supports genomic, cDNA, and protein-level variant annotation.
- **Core Function**: Transcript-based variant annotator.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda transvar`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
