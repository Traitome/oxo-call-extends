---
name: vcf-pg-loader
category: variant-calling
description: High-performance VCF to PostgreSQL loader with clinical-grade compliance
tags: [vcf-pg-loader, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/Zacharyr41/vcf-pg-loader/tree/main/docs"
---

## Concepts

- **Tool Overview**: vcf-pg-loader (v0.5.4) - vcf-pg-loader is a command-line tool for efficiently loading VCF variant data into PostgreSQL databases. It features streaming VCF parsing with cyvcf2, variant normalization using the vt algorithm, proper Number=A/R/G field handling during multi-allelic decomposition, and binary COPY protocol via asyncpg for maximum insert performance.
- **Core Function**: High-performance VCF to PostgreSQL loader with clinical-grade compliance
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vcf-pg-loader`

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
