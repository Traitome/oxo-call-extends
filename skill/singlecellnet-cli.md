---
name: singlecellnet-cli
category: utility
description: A set of command-line wrappers for the core functions in the SingleCellNet package.
tags: [singlecellnet-cli, utility]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/singlecellnet-cli"
---

## Concepts

- **Tool Overview**: singlecellnet-cli (v0.0.1) - A set of command-line wrappers for the core functions in the SingleCellNet package.
- **Core Function**: A set of command-line wrappers for the core functions in the SingleCellNet package.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda singlecellnet-cli`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `singlecellnet-cli -i <input_file> -o <output_file>`
**Explanation:** Run singlecellnet-cli with typical input and output options.
