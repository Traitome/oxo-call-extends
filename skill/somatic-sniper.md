---
name: somatic-sniper
category: variant-calling
description: A tool to call somatic single nucleotide variants.
tags: [somatic-sniper, variant-calling]
author: oxo-call-community
source_url: "https://github.com/genome/somatic-sniper/"
---

## Concepts

- **Tool Overview**: somatic-sniper (v1.0.5.0) - A tool to call somatic single nucleotide variants.
- **Core Function**: A tool to call somatic single nucleotide variants.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda somatic-sniper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `somatic-sniper -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run somatic-sniper with typical input and output options.
