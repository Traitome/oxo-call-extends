---
name: seshat
category: annotation
description: Tools for programmatically annotating VCFs with the Seshat TP53 database.
tags: [seshat, annotation, vcf]
author: oxo-call-community
source_url: "https://github.com/clintval/tp53"
---

## Concepts

- **Tool Overview**: seshat (v0.10.0) - Tools for programmatically annotating VCFs with the Seshat TP53 database.
- **Core Function**: Tools for programmatically annotating VCFs with the Seshat TP53 database.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seshat`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seshat -i <input.fasta> -o <output.gff>`
**Explanation:** Run seshat with typical input and output options.
