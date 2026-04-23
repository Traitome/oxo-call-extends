---
name: vtools
category: utility
description: Various tools operating over VCF files. Uses cyvcf2 and cython under the hood for speed
tags: [vtools, utility, vcf]
author: oxo-call-community
source_url: "https://github.com/LUMC/vtools"
---

## Concepts

- **Tool Overview**: vtools (v1.1.0) - Various tools operating over VCF files. Uses cyvcf2 and cython under the hood for speed
- **Core Function**: Various tools operating over VCF files. Uses cyvcf2 and cython under the hood for speed
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vtools`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
