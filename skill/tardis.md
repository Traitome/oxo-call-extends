---
name: tardis
category: hpc
description: Pre-processor for bioinformatics cluster job submission
tags: [tardis, hpc]
author: oxo-call-community
source_url: "https://github.com/AgResearch/tardis"
---

## Concepts

- **Tool Overview**: tardis (v1.0.19) - Pre-processor for bioinformatics cluster job submission
- **Core Function**: Pre-processor for bioinformatics cluster job submission
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tardis`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tardis -i <input_file> -o <output_file>`
**Explanation:** Run tardis with typical input and output options.
