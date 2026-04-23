---
name: super-focus
category: metagenomics
description: SUPER-FOCUS: A tool for agile functional analysis of shotgun metagenomic data
tags: [super-focus, metagenomics]
author: oxo-call-community
source_url: "https://edwards.sdsu.edu/SUPERFOCUS"
---

## Concepts

- **Tool Overview**: super-focus (v1.6) - SUPER-FOCUS: A tool for agile functional analysis of shotgun metagenomic data
- **Core Function**: SUPER-FOCUS: A tool for agile functional analysis of shotgun metagenomic data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda super-focus`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `super-focus -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run super-focus with typical input and output options.
