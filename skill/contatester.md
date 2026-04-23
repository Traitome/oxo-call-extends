---
name: contatester
category: formatting
description: Compute the Allelic Balance of a sample from a VCF file.
tags: [contatester, formatting, SAM, VCF]
author: oxo-call-community
source_url: "https://github.com/CNRGH/contatester"
---

## Concepts

- **Tool Overview**: contatester (v1.0.0) - Compute the Allelic Balance of a sample from a VCF file.
- **Core Function**: Contatester computes the Allelic Balance of a sample from a VCF file, check if a cross human contamination is present and estimate the degree of contamination, using pegasus for high efficiency.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda contatester`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.gff -o output.gtf`
**Explanation:** Convert between file formats
