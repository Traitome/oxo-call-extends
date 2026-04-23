---
name: severus
category: variant-calling
description: A tool for somatic structural variant calling using long reads
tags: [severus, variant-calling]
author: oxo-call-community
source_url: "https://github.com/KolmogorovLab/Severus"
---

## Concepts

- **Tool Overview**: severus (v1.7) - A tool for somatic structural variant calling using long reads
- **Core Function**: A tool for somatic structural variant calling using long reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda severus`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `severus -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run severus with typical input and output options.
