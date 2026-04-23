---
name: singularity
category: containerization
description: Singularity - Enabling users to have full control of their environment
tags: [singularity, containerization]
author: oxo-call-community
source_url: "http://singularity.lbl.gov"
---

## Concepts

- **Tool Overview**: singularity (v2.4.2) - Singularity - Enabling users to have full control of their environment
- **Core Function**: Singularity - Enabling users to have full control of their environment
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda singularity`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `singularity -i <input_file> -o <output_file>`
**Explanation:** Run singularity with typical input and output options.
