---
name: simple_sv_annotation
category: variant-calling
description: Simplify snpEff annotations for interesting cases
tags: [simple_sv_annotation, variant-calling]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/simple_sv_annotation"
---

## Concepts

- **Tool Overview**: simple_sv_annotation (v2019.02.18) - Simplify snpEff annotations for interesting cases
- **Core Function**: Simplify snpEff annotations for interesting cases
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda simple_sv_annotation`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `simple_sv_annotation -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run simple_sv_annotation with typical input and output options.
