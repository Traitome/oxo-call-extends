---
name: takeabreak
category: assembly
description: tool that can detect inversion breakpoints directly from raw NGS reads, without the need of any reference genome and without de novo assembling the genomes
tags: [takeabreak, assembly]
author: oxo-call-community
source_url: "https://colibread.inria.fr/software/takeabreak/"
---

## Concepts

- **Tool Overview**: takeabreak (v1.1.2) - tool that can detect inversion breakpoints directly from raw NGS reads, without the need of any reference genome and without de novo assembling the genomes
- **Core Function**: tool that can detect inversion breakpoints directly from raw NGS reads, without the need of any reference genome and without de novo assembling the genomes
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda takeabreak`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `takeabreak -i <reads.fastq> -o <output_dir>`
**Explanation:** Run takeabreak with typical input and output options.
