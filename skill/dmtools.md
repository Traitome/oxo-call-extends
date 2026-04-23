---
name: dmtools
category: utility
description: DMTools - Utilities for DNA methylation data processing.
tags: [dmtools, utility, methylation, epigenomics]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DMTools - Collection of utilities for DNA methylation data analysis.
- **Core Function**: Processes and analyzes DNA methylation data from bisulfite sequencing.
- **Input/Output**: Expects methylation call files; outputs processed methylation data.
- **Installation**: `conda install -c bioconda dmtools`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires methylation data from bisulfite sequencing.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dmtools extract --input meth_calls.bed --output methylation.tsv`
**Explanation:** Extracts and processes methylation data.
