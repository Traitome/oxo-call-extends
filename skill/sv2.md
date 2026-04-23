---
name: sv2
category: variant-calling
description: Support Vector Structural Variation Genotyper
tags: [sv2, variant-calling]
author: oxo-call-community
source_url: "https://github.com/dantaki/SV2"
---

## Concepts

- **Tool Overview**: sv2 (v1.4.3.4) - Support Vector Structural Variation Genotyper
- **Core Function**: Support Vector Structural Variation Genotyper
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sv2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sv2 -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run sv2 with typical input and output options.
