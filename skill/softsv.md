---
name: softsv
category: utility
description: SoftSV is a tool for the detection of small and large deletions, inversions, tandem duplications and translocations from paired-end sequencing data.
tags: [softsv, utility, tsv]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/softsv"
---

## Concepts

- **Tool Overview**: softsv (v1.4.2) - SoftSV is a tool for the detection of small and large deletions, inversions, tandem duplications and translocations from paired-end sequencing data.
- **Core Function**: SoftSV is a tool for the detection of small and large deletions, inversions, tandem duplications and translocations from paired-end sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda softsv`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `softsv -i <input_file> -o <output_file>`
**Explanation:** Run softsv with typical input and output options.
