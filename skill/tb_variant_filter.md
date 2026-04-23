---
name: tb_variant_filter
category: variant-calling
description: VCF variant filter optimised for filter M. tuberculosis H37Rv variants
tags: [tb_variant_filter, variant-calling, vcf]
author: oxo-call-community
source_url: "http://github.com/COMBAT-TB/tb_variant_filter"
---

## Concepts

- **Tool Overview**: tb_variant_filter (v0.4.0) - VCF variant filter optimised for filter M. tuberculosis H37Rv variants
- **Core Function**: VCF variant filter optimised for filter M. tuberculosis H37Rv variants
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tb_variant_filter`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tb_variant_filter -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run tb_variant_filter with typical input and output options.
