---
name: svarp
category: variant-calling
description: Pangenome-based structural variant discovery (SVarp)
tags: [svarp, variant-calling]
author: oxo-call-community
source_url: "https://github.com/asylvz/SVarp"
---

## Concepts

- **Tool Overview**: svarp (v1.2.0) - Pangenome-based structural variant discovery (SVarp)
- **Core Function**: Pangenome-based structural variant discovery (SVarp)
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svarp`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svarp -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svarp with typical input and output options.
