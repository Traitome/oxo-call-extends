---
name: scpred-cli
category: utility
description: A set of command-line wrappers for the core functions in the scPred package.
tags: [scpred-cli, utility]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/scPred-cli"
---

## Concepts

- **Tool Overview**: scpred-cli (v0.1.0) - A set of command-line wrappers for the core functions in the scPred package.
- **Core Function**: A set of command-line wrappers for the core functions in the scPred package.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scpred-cli`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scpred-cli -i <input_file> -o <output_file>`
**Explanation:** Run scpred-cli with typical input and output options.
