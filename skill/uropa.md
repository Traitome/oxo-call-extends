---
name: uropa
category: variant-calling
description: UROPA (Universal RObust Peak Annotator) is a command line based tool, intended for genomic region annotation from e.g. peak calling. It detects the most appropriate annotation by taking parameters such as feature type, anchor, direction and strand into account. Furthermore, it allows filtering for GTF attribute values, e.g. protein_coding.
tags: [uropa, variant-calling]
author: oxo-call-community
source_url: "http://uropa-manual.readthedocs.io"
---

## Concepts

- **Tool Overview**: uropa (v4.0.3) - UROPA (Universal RObust Peak Annotator) is a command line based tool, intended for genomic region annotation from e.g. peak calling. It detects the most appropriate annotation by taking parameters such as feature type, anchor, direction and strand into account. Furthermore, it allows filtering for GTF attribute values, e.g. protein_coding.
- **Core Function**: UROPA (Universal RObust Peak Annotator) is a command line based tool, intended for genomic region annotation from e.g. peak calling. It detects the most appropriate annotation by taking parameters such as feature type, anchor, direction and strand into account. Furthermore, it allows filtering for GTF attribute values, e.g. protein_coding.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda uropa`

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
