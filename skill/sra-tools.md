---
name: sra-tools
category: utility
description: The SRA Toolkit and SDK from NCBI.
tags: [sra-tools, utility]
author: oxo-call-community
source_url: "https://github.com/ncbi/sra-tools/wiki"
---

## Concepts

- **Tool Overview**: sra-tools (v3.4.1) - The SRA Toolkit and SDK from NCBI.
- **Core Function**: The SRA Toolkit and SDK from NCBI.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sra-tools`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sra-tools -i <input_file> -o <output_file>`
**Explanation:** Run sra-tools with typical input and output options.
