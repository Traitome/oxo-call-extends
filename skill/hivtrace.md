---
name: hivtrace
category: hpc
description: HIV TRACE is an application that identifies potential transmission clusters within a supplied FASTA file with an option to find potential links against the Los Alamos HIV Sequence Database.
tags: [hivtrace, hpc, FASTA]
author: oxo-call-community
source_url: "https://github.com/veg/hivtrace"
---

## Concepts

- **Tool Overview**: hivtrace (v1.5.0) - HIV TRACE is an application that identifies potential transmission clusters within a supplied FASTA file with an option to find potential links against the Los Alamos HIV Sequence Database.
- **Core Function**: Provides functionality for hpc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hivtrace`

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
