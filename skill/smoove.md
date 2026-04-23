---
name: smoove
category: variant-calling
description: structural variant calling and genotyping with existing tools, but, smoothly
tags: [smoove, variant-calling]
author: oxo-call-community
source_url: "https://github.com/brentp/smoove"
---

## Concepts

- **Tool Overview**: smoove (v0.2.8) - structural variant calling and genotyping with existing tools, but, smoothly
- **Core Function**: structural variant calling and genotyping with existing tools, but, smoothly
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smoove`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smoove -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run smoove with typical input and output options.
