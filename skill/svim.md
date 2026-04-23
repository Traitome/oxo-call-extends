---
name: svim
category: variant-calling
description: SVIM is a structural variant caller for long reads.
tags: [svim, variant-calling]
author: oxo-call-community
source_url: "https://github.com/eldariont/svim/wiki"
---

## Concepts

- **Tool Overview**: svim (v2.0.0) - SVIM is a structural variant caller for long reads.
- **Core Function**: SVIM is a structural variant caller for long reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svim`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svim -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svim with typical input and output options.
