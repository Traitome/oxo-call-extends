---
name: tadarida-c
category: metagenomics
description: Tadarida-C (Toolbox for Animal Detection on Acoustic Recordings - Classification part) for Galaxy use.
tags: [tadarida-c, metagenomics]
author: oxo-call-community
source_url: "https://github.com/YvesBas/Tadarida-C"
---

## Concepts

- **Tool Overview**: tadarida-c (v1.2) - Tadarida-C (Toolbox for Animal Detection on Acoustic Recordings - Classification part) for Galaxy use.
- **Core Function**: Tadarida-C (Toolbox for Animal Detection on Acoustic Recordings - Classification part) for Galaxy use.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tadarida-c`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tadarida-c -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run tadarida-c with typical input and output options.
