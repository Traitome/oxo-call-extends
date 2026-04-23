---
name: dnapi
category: utility
description: DNApi - DNA primer design tool.
tags: [dnapi, utility, primer-design, pcr]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DNApi - Tool for designing PCR primers.
- **Core Function**: Designs optimal primers for PCR amplification.
- **Input/Output**: Expects target sequences; outputs primer designs with properties.
- **Installation**: `conda install -c bioconda dnapi`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires target DNA sequences.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dnapi design --input target.fa --output primers.tsv`
**Explanation:** Designs PCR primers for target sequences.
