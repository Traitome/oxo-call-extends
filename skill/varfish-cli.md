---
name: varfish-cli
category: programming
description: Command line interface to VarFish via REST API
tags: [varfish-cli, programming]
author: oxo-call-community
source_url: "https://github.com/bihealth/varfish-cli"
---

## Concepts

- **Tool Overview**: varfish-cli (v0.7.0) - Command line interface to VarFish via REST API
- **Core Function**: Command line interface to VarFish via REST API
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda varfish-cli`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
