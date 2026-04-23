---
name: shigapass
category: annotation
description: ShigaPass: An in silico tool to predict Shigella serotypes
tags: [shigapass, annotation]
author: oxo-call-community
source_url: "https://github.com/imanyass/ShigaPass/"
---

## Concepts

- **Tool Overview**: shigapass (v1.5.0) - ShigaPass: An in silico tool to predict Shigella serotypes
- **Core Function**: ShigaPass: An in silico tool to predict Shigella serotypes
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shigapass`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shigapass -i <input.fasta> -o <output.gff>`
**Explanation:** Run shigapass with typical input and output options.
