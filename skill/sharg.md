---
name: sharg
category: formatting
description: A modern argument parser for C++ tools.
tags: [sharg, formatting]
author: oxo-call-community
source_url: "https://docs.seqan.de/sharg/1.2.2/index.html"
---

## Concepts

- **Tool Overview**: sharg (v1.2.2) - A modern argument parser for C++ tools.
- **Core Function**: A modern argument parser for C++ tools.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sharg`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sharg -i <input_file> -o <output_file>`
**Explanation:** Run sharg with typical input and output options.
