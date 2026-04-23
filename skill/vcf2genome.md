---
name: vcf2genome
category: variant-calling
description: A tool to create a draft genome file out of a GATK VCF file and enabling users to filter the VCF in a single step.
tags: [vcf2genome, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/apeltzer/vcf2genome"
---

## Concepts

- **Tool Overview**: vcf2genome (v0.91) - A tool to create a draft genome file out of a GATK VCF file and enabling users to filter the VCF in a single step.
- **Core Function**: A tool to create a draft genome file out of a GATK VCF file and enabling users to filter the VCF in a single step.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vcf2genome`

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
