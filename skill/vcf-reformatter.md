---
name: vcf-reformatter
category: variant-calling
description: Fast VCF file parser and reformatter with VEP and SnpEff annotation support
tags: [vcf-reformatter, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/flalom/vcf-reformatter/blob/main/README.md"
---

## Concepts

- **Tool Overview**: vcf-reformatter (v0.3.0) - A Rust command-line tool for parsing and reformatting VCF (Variant Call Format) files, with support for VEP (Variant Effect Predictor) and SnpEff annotations. This tool flattens complex VCF files into tab-separated values (TSV) format for easier downstream analysis.
- **Core Function**: Fast VCF file parser and reformatter with VEP and SnpEff annotation support
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vcf-reformatter`

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
