---
name: spacepharer
category: genome-editing
description: SpacePHARER: Sensitive identification of phages from CRISPR spacers in prokaryotic hosts
tags: [spacepharer, genome-editing]
author: oxo-call-community
source_url: "https://github.com/soedinglab/spacepharer"
---

## Concepts

- **Tool Overview**: spacepharer (v5.c2e680a) - SpacePHARER: Sensitive identification of phages from CRISPR spacers in prokaryotic hosts
- **Core Function**: SpacePHARER: Sensitive identification of phages from CRISPR spacers in prokaryotic hosts
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spacepharer`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spacepharer -i <input.fasta> -g <guide.fa> -o <output_dir>`
**Explanation:** Run spacepharer with typical input and output options.
