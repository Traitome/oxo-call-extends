---
name: hmftools-sage
category: variant-calling
description: SAGE is a somatic SNV, MNV and small INDEL caller optimised 100x tumor / 40x normal coverage, but has a flexible set of filters that can be adapted to lower or higher depth coverage.
tags: [hmftools-sage, variant-calling]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/sage"
---

## Concepts

- **Tool Overview**: hmftools-sage (v4.2) - SAGE is a somatic SNV, MNV and small INDEL caller optimised 100x tumor / 40x normal coverage, but has a flexible set of filters that can be adapted to lower or higher depth coverage.
- **Core Function**: Provides functionality for variant-calling tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hmftools-sage`

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
