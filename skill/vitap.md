---
name: vitap
category: metagenomics
description: Viral Taxonomic Assignment Pipeline
tags: [vitap, metagenomics]
author: oxo-call-community
source_url: "https://github.com/DrKaiyangZheng/VITAP/blob/main/README.md"
---

## Concepts

- **Tool Overview**: vitap (v1.12) - Viral Taxonomic Assignment Pipeline (VITAP) is a tool designed to address the growing need for accurate and comprehensive taxonomic assignments of DNA and RNA viral sequences based on ICTV VMR and UniRef90.
- **Core Function**: Viral Taxonomic Assignment Pipeline
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vitap`

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
