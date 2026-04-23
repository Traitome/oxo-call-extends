---
name: shapeit5
category: variant-calling
description: Fast and accurate method for estimation of haplotypes (phasing).
tags: [shapeit5, variant-calling]
author: oxo-call-community
source_url: "https://odelaneau.github.io/shapeit5"
---

## Concepts

- **Tool Overview**: shapeit5 (v5.1.1) - Fast and accurate method for estimation of haplotypes (phasing).
- **Core Function**: Fast and accurate method for estimation of haplotypes (phasing).
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shapeit5`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shapeit5 -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run shapeit5 with typical input and output options.
