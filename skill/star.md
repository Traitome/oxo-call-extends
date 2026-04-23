---
name: star
category: alignment
description: An RNA-seq read aligner.
tags: [star, alignment]
author: oxo-call-community
source_url: "https://github.com/alexdobin/STAR/blob/2.7.11b/doc/STARmanual.pdf"
---

## Concepts

- **Tool Overview**: star (v2.7.11b) - An RNA-seq read aligner.
- **Core Function**: An RNA-seq read aligner.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda star`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `star -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run star with typical input and output options.
