---
name: tigmint
category: assembly
description: Correct misassemblies using linked or long reads
tags: [tigmint, assembly]
author: oxo-call-community
source_url: "https://github.com/bcgsc/tigmint#readme"
---

## Concepts

- **Tool Overview**: tigmint (v1.2.10) - Correct misassemblies using linked or long reads
- **Core Function**: Correct misassemblies using linked or long reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tigmint`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tigmint -i <reads.fastq> -o <output_dir>`
**Explanation:** Run tigmint with typical input and output options.
