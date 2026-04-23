---
name: sodar-cli
category: utility
description: Command line interface to SODAR via REST API
tags: [sodar-cli, utility]
author: oxo-call-community
source_url: "https://github.com/bihealth/sodar-cli"
---

## Concepts

- **Tool Overview**: sodar-cli (v0.1.0) - Command line interface to SODAR via REST API
- **Core Function**: Command line interface to SODAR via REST API
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sodar-cli`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sodar-cli -i <input_file> -o <output_file>`
**Explanation:** Run sodar-cli with typical input and output options.
