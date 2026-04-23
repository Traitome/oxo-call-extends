---
name: dkfz-bias-filter
category: variant-calling
description: DKFZ bias filter flags SNVs that appear to be biased based on variant read support.
tags: [dkfz-bias-filter, variant-calling, filtering, bias, snv]
author: oxo-call-community
source_url: "https://github.com/eilslabs/DKFZBiasFilter"
---

## Concepts

- **Tool Overview**: DKFZ Bias Filter v1.2.3a - Filters SNVs showing sequence context bias in variant calls.
- **Core Function**: Flags and filters variant calls that show evidence of sequencing or alignment bias.
- **Input/Output**: Expects VCF files; outputs filtered VCF with bias annotations.
- **Installation**: `conda install -c bioconda dkfz-bias-filter`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires VCF with variant calls.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dkfz-bias-filter --input variants.vcf --output filtered.vcf`
**Explanation:** Filters biased SNVs from variant calls.
