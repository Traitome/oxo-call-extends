---
name: tapestry
category: assembly
description: Validate and edit small eukaryotic genome assemblies
tags: [tapestry, assembly]
author: oxo-call-community
source_url: "https://github.com/johnomics/tapestry"
---

## Concepts

- **Tool Overview**: tapestry (v1.0.1) - Validate and edit small eukaryotic genome assemblies
- **Core Function**: Validate and edit small eukaryotic genome assemblies
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tapestry`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tapestry -i <reads.fastq> -o <output_dir>`
**Explanation:** Run tapestry with typical input and output options.
