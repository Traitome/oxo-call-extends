---
name: hmftools-gripss
category: qc
description: GRIPSS applies a set of filtering and post processing steps on GRIDSS paired tumor-normal output to produce a high confidence set of somatic SV for a tumor sample.
tags: [hmftools-gripss, qc, SAM]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/gripss"
---

## Concepts

- **Tool Overview**: hmftools-gripss (v2.4) - GRIPSS applies a set of filtering and post processing steps on GRIDSS paired tumor-normal output to produce a high confidence set of somatic SV for a tumor sample.
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hmftools-gripss`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
