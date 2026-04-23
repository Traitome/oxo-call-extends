---
name: siann
category: utility
description: SIANN was created to allow creation of local small sets of bacterial/viral genomes to perform strain level differentiation from fastq data
tags: [siann, utility, fastq]
author: oxo-call-community
source_url: "https://github.com/signaturescience/siann/wiki"
---

## Concepts

- **Tool Overview**: siann (v1.3) - SIANN was created to allow creation of local small sets of bacterial/viral genomes to perform strain level differentiation from fastq data
- **Core Function**: SIANN was created to allow creation of local small sets of bacterial/viral genomes to perform strain level differentiation from fastq data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda siann`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `siann -i <input_file> -o <output_file>`
**Explanation:** Run siann with typical input and output options.
