---
name: xcftools
category: utility
description: Provides xcf2pnm, xcf2png, and xcfinfo binaries
tags: [xcftools, utility]
author: oxo-call-community
source_url: "https://github.com/j-jorge/xcftools"
---

## Concepts

- **Tool Overview**: xcftools (v1.0.7) - Provides xcf2pnm, xcf2png, and xcfinfo binaries
- **Core Function**: Provides xcf2pnm, xcf2png, and xcfinfo binaries
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda xcftools`

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
