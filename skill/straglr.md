---
name: straglr
category: variant-calling
description: Short-tandem repeat genotyping using long reads
tags: [straglr, variant-calling]
author: oxo-call-community
source_url: "https://github.com/BirolLab/straglr"
---

## Concepts

- **Tool Overview**: straglr (v1.5.6) - Short-tandem repeat genotyping using long reads
- **Core Function**: Short-tandem repeat genotyping using long reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda straglr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `straglr -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run straglr with typical input and output options.
