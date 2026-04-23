---
name: simug
category: variant-calling
description: A simple, flexible, and powerful tool to simulate genome sequences with pre-defined or random genomic variants.
tags: [simug, variant-calling]
author: oxo-call-community
source_url: "https://github.com/yjx1217/simuG"
---

## Concepts

- **Tool Overview**: simug (v1.0.1) - A simple, flexible, and powerful tool to simulate genome sequences with pre-defined or random genomic variants.
- **Core Function**: A simple, flexible, and powerful tool to simulate genome sequences with pre-defined or random genomic variants.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda simug`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `simug -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run simug with typical input and output options.
