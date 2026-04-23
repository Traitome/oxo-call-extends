---
name: igda-script
category: variant-calling
description: The wrapper script of iGDA to detect and phase minor SNVs from long-read sequencing data
tags: [igda-script, variant-calling]
author: oxo-call-community
source_url: "https://github.com/zhixingfeng/shell"
---

## Concepts

- **Tool Overview**: igda-script (v1.0.1) - The wrapper script of iGDA to detect and phase minor SNVs from long-read sequencing data
- **Core Function**: Provides functionality for variant-calling tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda igda-script`

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
