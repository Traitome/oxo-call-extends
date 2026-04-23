---
name: lefse
category: metagenomics
description: LDA Effect Size (LEfSe) (Segata et. al 2010) is an algorithm for high-dimensional biomarker discovery and explanation that identifies genomic features (genes, pathways, or taxa) characterizing the differences between two or more biological conditions.
tags: [lefse, metagenomics]
author: oxo-call-community
source_url: "https://github.com/SegataLab/lefse"
---

## Concepts

- **Tool Overview**: lefse v1.1.2 - LDA Effect Size (LEfSe) (Segata et. al 2010) is an algorithm for high-dimensional biomarker discovery and explanation that identifies genomic features (genes, pathways, or taxa) characterizing the differences between two or more biological conditions..
- **Core Function**: LDA Effect Size (LEfSe) (Segata et. al 2010) is an algorithm for high-dimensional biomarker discovery and explanation that identifies genomic features (genes, pathways, or taxa) characterizing the differences between two or more biological conditions.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda lefse`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Run LEfSe
**Args:** `lefse_run.py input.txt output.res`
**Explanation:** Identifies biomarkers with significant differential abundance.

