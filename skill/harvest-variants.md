---
name: harvest-variants
category: variant-calling
description: Harvest Variants is a pipeline for variant calling on SARS-CoV-2 samples
tags: [harvest-variants, variant-calling, SAM]
author: oxo-call-community
source_url: "https://gitlab.com/treangenlab/sars-cov-2-harvest-variants"
---

## Concepts

- **Tool Overview**: harvest-variants (v1.1.0) - Harvest Variants is a pipeline for variant calling on SARS-CoV-2 samples
- **Core Function**: Provides functionality for variant-calling tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda harvest-variants`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
