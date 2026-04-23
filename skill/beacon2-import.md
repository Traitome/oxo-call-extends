---
name: beacon2-import
category: variant-calling
description: Seamlessly import and query genomic variant data from a beacon
tags: [beacon2-import, variant-calling]
author: oxo-call-community
source_url: "https://pypi.org/project/beacon2-import/"
---

## Concepts

- **Tool Overview**: beacon2-import (v2.2.4) - Seamlessly import and query genomic variant data from a beacon
- **Core Function**: Effortlessly import genetic variants from targeted Galaxy histories or local repositories into your beacon instance with our utility. Simplify querying and analysis of genetic data, enabling comprehen...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda beacon2-import`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Call variants from aligned reads
