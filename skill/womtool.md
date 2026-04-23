---
name: womtool
category: utility
description: Command line utilities for interacting with WDL
tags: [womtool, utility]
author: oxo-call-community
source_url: "https://cromwell.readthedocs.io/en/develop/WOMtool/"
---

## Concepts

- **Tool Overview**: womtool (v61) - Command line utilities for interacting with WDL
- **Core Function**: Command line utilities for interacting with WDL
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda womtool`

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
