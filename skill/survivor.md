---
name: survivor
category: qc
description: Toolset for SV simulation, comparison and filtering.
tags: [survivor, qc]
author: oxo-call-community
source_url: "https://github.com/fritzsedlazeck/SURVIVOR"
---

## Concepts

- **Tool Overview**: survivor (v1.0.7) - Toolset for SV simulation, comparison and filtering.
- **Core Function**: Toolset for SV simulation, comparison and filtering.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda survivor`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `survivor -i <input.fastq> -o <output_dir>`
**Explanation:** Run survivor with typical input and output options.
