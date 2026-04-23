---
name: vcf-annotator
category: variant-calling
description: Use the reference GenBank file to add biological annotations to the variant calls in a VCF.
tags: [vcf-annotator, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/rpetit3/vcf-annotator"
---

## Concepts

- **Tool Overview**: vcf-annotator (v1.0.0) - Use the reference GenBank file to add biological annotations to the variant calls in a VCF.
- **Core Function**: Use the reference GenBank file to add biological annotations to the variant calls in a VCF.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vcf-annotator`

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
