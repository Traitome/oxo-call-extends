---
name: stemcnv-check
category: variant-calling
description: StemCNV-check: CNV Based Quality Control Workflow for Stem Cell SNP Array Data.
tags: [stemcnv-check, variant-calling]
author: oxo-call-community
source_url: "https://stemcnv-check.readthedocs.io"
---

## Concepts

- **Tool Overview**: stemcnv-check (v1.0.0) - StemCNV-check: CNV Based Quality Control Workflow for Stem Cell SNP Array Data.
- **Core Function**: StemCNV-check: CNV Based Quality Control Workflow for Stem Cell SNP Array Data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stemcnv-check`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stemcnv-check -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run stemcnv-check with typical input and output options.
