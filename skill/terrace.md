---
name: terrace
category: assembly
description: TERRACE is an assembler for circular RNAs.
tags: [terrace, assembly]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/TERRACE"
---

## Concepts

- **Tool Overview**: terrace (v1.1.2) - TERRACE is an assembler for circular RNAs.
- **Core Function**: TERRACE is an assembler for circular RNAs.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda terrace`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `terrace -i <reads.fastq> -o <output_dir>`
**Explanation:** Run terrace with typical input and output options.
