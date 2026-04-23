---
name: svdss
category: variant-calling
description: Structural Variant Discovery from Sample-specific Strings.
tags: [svdss, variant-calling, sam]
author: oxo-call-community
source_url: "https://github.com/Parsoa/SVDSS/blob/v2.1.1/README.md"
---

## Concepts

- **Tool Overview**: svdss (v2.1.1) - Structural Variant Discovery from Sample-specific Strings.
- **Core Function**: Structural Variant Discovery from Sample-specific Strings.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svdss`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svdss -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svdss with typical input and output options.
