---
name: shorah
category: assembly
description: The Short Reads Assembly into Haplotypes (ShoRAH) program for inferring viral haplotypes from NGS data
tags: [shorah, assembly]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/shorah"
---

## Concepts

- **Tool Overview**: shorah (v1.99.2) - The Short Reads Assembly into Haplotypes (ShoRAH) program for inferring viral haplotypes from NGS data
- **Core Function**: The Short Reads Assembly into Haplotypes (ShoRAH) program for inferring viral haplotypes from NGS data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shorah`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shorah -i <reads.fastq> -o <output_dir>`
**Explanation:** Run shorah with typical input and output options.
