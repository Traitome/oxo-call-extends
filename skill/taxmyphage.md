---
name: taxmyphage
category: metagenomics
description: Script to assign taxonomy to a bacteriophage at the genus and species level.
tags: [taxmyphage, metagenomics]
author: oxo-call-community
source_url: "https://github.com/amillard/tax_myPHAGE"
---

## Concepts

- **Tool Overview**: taxmyphage (v0.3.7) - Script to assign taxonomy to a bacteriophage at the genus and species level.
- **Core Function**: Script to assign taxonomy to a bacteriophage at the genus and species level.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxmyphage`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxmyphage -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run taxmyphage with typical input and output options.
