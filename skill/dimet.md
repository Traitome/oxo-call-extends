---
name: dimet
category: metagenomics
description: DIMET - Differential analysis of metabolomics data.
tags: [dimet, metagenomics, metabolomics, differential-analysis]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DIMET - Tool for differential analysis of metabolomics data.
- **Core Function**: Performs statistical differential analysis on metabolomics datasets.
- **Input/Output**: Expects metabolomics abundance tables; outputs differential metabolite results.
- **Installation**: `conda install -c bioconda dimet`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires metabolomics data in appropriate tabular format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dimet --input metabolites.tsv --output diff_results.tsv`
**Explanation:** Performs differential analysis on metabolomics data.
