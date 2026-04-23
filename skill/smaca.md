---
name: smaca
category: population-genomics
description: smaca is a python tool to detect putative SMA carriers and estimate the absolute SMN1 copy-number in a population.
tags: [smaca, population-genomics]
author: oxo-call-community
source_url: "https://github.com/babelomics/SMAca"
---

## Concepts

- **Tool Overview**: smaca (v1.2.4rc11) - smaca is a python tool to detect putative SMA carriers and estimate the absolute SMN1 copy-number in a population.
- **Core Function**: smaca is a python tool to detect putative SMA carriers and estimate the absolute SMN1 copy-number in a population.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smaca`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smaca -i <input.vcf> -o <output_dir>`
**Explanation:** Run smaca with typical input and output options.
