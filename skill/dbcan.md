---
name: dbcan
category: annotation
description: Standalone version of dbCAN annotation tool for automated CAZyme annotation.
tags: [dbcan, annotation]
author: oxo-call-community
source_url: "https://run-dbcan.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: dbcan (v5.2.8) - Standalone version of dbCAN annotation tool for automated CAZyme annotation.
- **Core Function**: Standalone version of dbCAN annotation tool for automated CAZyme annotation.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda dbcan`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i assembly.fasta -o annotation.gff`
**Explanation:** Annotate genomic features
