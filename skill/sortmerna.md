---
name: sortmerna
category: utility
description: SortMeRNA is a biological sequence analysis tool for filtering, mapping and OTU-picking NGS reads.
tags: [sortmerna, utility]
author: oxo-call-community
source_url: "https://sortmerna.readthedocs.io"
---

## Concepts

- **Tool Overview**: sortmerna (v4.3.7) - SortMeRNA is a biological sequence analysis tool for filtering, mapping and OTU-picking NGS reads.
- **Core Function**: SortMeRNA is a biological sequence analysis tool for filtering, mapping and OTU-picking NGS reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sortmerna`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sortmerna -i <input_file> -o <output_file>`
**Explanation:** Run sortmerna with typical input and output options.
