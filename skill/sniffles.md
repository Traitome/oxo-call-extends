---
name: sniffles
category: variant-calling
description: Sniffles is a structural variation caller using third generation sequencing (PacBio or Oxford Nanopore).
tags: [sniffles, variant-calling]
author: oxo-call-community
source_url: "https://github.com/fritzsedlazeck/Sniffles/wiki"
---

## Concepts

- **Tool Overview**: sniffles (v2.7.5) - Sniffles is a structural variation caller using third generation sequencing (PacBio or Oxford Nanopore).
- **Core Function**: Sniffles is a structural variation caller using third generation sequencing (PacBio or Oxford Nanopore).
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sniffles`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sniffles -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sniffles with typical input and output options.
