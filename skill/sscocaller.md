---
name: sscocaller
category: variant-calling
description: Haplotyping single-cell DNA sequenced gamete cells.
tags: [sscocaller, variant-calling]
author: oxo-call-community
source_url: "https://gitlab.svi.edu.au/biocellgen-public/sscocaller"
---

## Concepts

- **Tool Overview**: sscocaller (v0.2.2) - Haplotyping single-cell DNA sequenced gamete cells.
- **Core Function**: Haplotyping single-cell DNA sequenced gamete cells.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sscocaller`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sscocaller -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sscocaller with typical input and output options.
