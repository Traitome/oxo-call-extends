---
name: vcf2maf
category: variant-calling
description: Convert a VCF into a MAF where each variant is annotated to only one of all possible gene isoforms.
tags: [vcf2maf, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/mskcc/vcf2maf"
---

## Concepts

- **Tool Overview**: vcf2maf (v1.6.22) - Convert a VCF into a MAF where each variant is annotated to only one of all possible gene isoforms.
- **Core Function**: Convert a VCF into a MAF where each variant is annotated to only one of all possible gene isoforms.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vcf2maf`

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
