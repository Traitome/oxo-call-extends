---
name: ucsc-bedclip
category: utility
description: Remove lines from bed file that refer to off-chromosome locations.
tags: [ucsc-bedclip, utility]
author: oxo-call-community
source_url: "https://github.com/ucscGenomeBrowser/kent/blob/v482_base/README"
---

## Concepts

- **Tool Overview**: ucsc-bedclip (v482) - Remove lines from bed file that refer to off-chromosome locations.
- **Core Function**: Remove lines from bed file that refer to off-chromosome locations.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-bedclip`

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
