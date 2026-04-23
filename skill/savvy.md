---
name: savvy
category: variant-calling
description: Interface to various variant calling formats.
tags: ["savvy", "variant-calling"]
author: oxo-call-community
source_url: "https://github.com/statgen/savvy"
---

## Concepts

- **Tool Overview**: Interface to various variant calling formats. (version 2.2.0)
- **Core Function**: Processes bioinformatics data related to variant-calling
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda savvy`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Call variants
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Identifies variants from aligned reads.

