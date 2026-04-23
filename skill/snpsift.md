---
name: snpsift
category: variant-calling
description: Toolbox that allows you to filter and manipulate annotated files
tags: [snpsift, variant-calling]
author: oxo-call-community
source_url: "http://snpeff.sourceforge.net/SnpSift.html"
---

## Concepts

- **Tool Overview**: snpsift (v5.4.0c) - Toolbox that allows you to filter and manipulate annotated files
- **Core Function**: Toolbox that allows you to filter and manipulate annotated files
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snpsift`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snpsift -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run snpsift with typical input and output options.
