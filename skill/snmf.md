---
name: snmf
category: population-genomics
description: Fast and efficient program for estimating individual admixture coefficients based on sparse non-negative matrix factorization and population genetics
tags: [snmf, population-genomics]
author: oxo-call-community
source_url: "http://membres-timc.imag.fr/Olivier.Francois/snmf/index.htm"
---

## Concepts

- **Tool Overview**: snmf (v1.2) - Fast and efficient program for estimating individual admixture coefficients based on sparse non-negative matrix factorization and population genetics
- **Core Function**: Fast and efficient program for estimating individual admixture coefficients based on sparse non-negative matrix factorization and population genetics
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snmf`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snmf -i <input.vcf> -o <output_dir>`
**Explanation:** Run snmf with typical input and output options.
