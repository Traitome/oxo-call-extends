---
name: music-deconvolution
category: expression
description: Multi-subject single cell deconvolution
tags: [music-deconvolution, expression, deconvolution, single-cell, bulk-tissue]
author: oxo-call-community
source_url: "https://github.com/xuranw/MuSiC"
---

## Concepts

- **Tool Overview**: MuSiC v0.1.1 - multi-subject single cell deconvolution for bulk tissue cell type proportion estimation.
- **Core Function**: Estimates bulk tissue cell type proportions using multi-subject single cell expression as reference.
- **Input/Output**: Takes bulk expression data and single-cell reference; outputs estimated cell type proportions.
- **Installation**: `conda install -c bioconda music-deconvolution`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly formatted single-cell and bulk expression matrices.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `--bulk bulk_expr.tsv --sc sc_ref.tsv --output proportions.tsv`
**Explanation:** Estimates cell type proportions from bulk tissue using single-cell reference.
