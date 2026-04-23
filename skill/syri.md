---
name: syri
category: assembly
description: Synteny and rearrangement identifier between whole-genome assemblies.
tags: [syri, assembly]
author: oxo-call-community
source_url: "https://schneebergerlab.github.io/syri"
---

## Concepts

- **Tool Overview**: syri (v1.7.1) - Synteny and rearrangement identifier between whole-genome assemblies.
- **Core Function**: Synteny and rearrangement identifier between whole-genome assemblies.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda syri`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `syri -i <reads.fastq> -o <output_dir>`
**Explanation:** Run syri with typical input and output options.
