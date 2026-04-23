---
name: diapysef
category: annotation
description: Analysis, conversion and visualization of diaPASEF data.
tags: [diapysef, annotation, proteomics, dia-pasef, mass-spectrometry]
author: oxo-call-community
source_url: "https://github.com/Roestlab/dia-pasef"
---

## Concepts

- **Tool Overview**: diaPASEF v1.0.10 - Python tool for analysis, conversion and visualization of diaPASEF mass spectrometry data.
- **Core Function**: Processes and visualizes data-independent acquisition with parallel accumulation-serial fragmentation (diaPASEF) data.
- **Input/Output**: Expects Bruker diaPASEF .d files; outputs converted and analyzed data.
- **Installation**: `conda install -c bioconda diapysef`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Bruker diaPASEF format data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `diapysef convert --input sample.d --output sample.mzml`
**Explanation:** Converts diaPASEF data for downstream analysis.
