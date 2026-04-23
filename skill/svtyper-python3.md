---
name: svtyper-python3
category: variant-calling
description: Bayesian genotyper for structural variants
tags: [svtyper-python3, variant-calling]
author: oxo-call-community
source_url: "https://github.com/hall-lab/svtyper"
---

## Concepts

- **Tool Overview**: svtyper-python3 (v0.7.1) - Bayesian genotyper for structural variants
- **Core Function**: Bayesian genotyper for structural variants
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svtyper-python3`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svtyper-python3 -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svtyper-python3 with typical input and output options.
