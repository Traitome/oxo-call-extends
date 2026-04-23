---
name: trim-galore
category: qc
description: Trim Galore! is a wrapper script to automate quality and adapter trimming as well as quality control
tags: [trim-galore, qc]
author: oxo-call-community
source_url: "https://github.com/FelixKrueger/TrimGalore"
---

## Concepts

- **Tool Overview**: trim-galore (v0.6.11) - Trim Galore! is a wrapper script to automate quality and adapter trimming as well as quality control
- **Core Function**: Trim Galore! is a wrapper script to automate quality and adapter trimming as well as quality control
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda trim-galore`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
