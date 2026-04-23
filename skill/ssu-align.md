---
name: ssu-align
category: alignment
description: SSU-ALIGN: structural alignment of SSU rRNA sequences
tags: [ssu-align, alignment]
author: oxo-call-community
source_url: "http://eddylab.org/software/ssu-align/"
---

## Concepts

- **Tool Overview**: ssu-align (v0.1.1) - SSU-ALIGN: structural alignment of SSU rRNA sequences
- **Core Function**: SSU-ALIGN: structural alignment of SSU rRNA sequences
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda ssu-align`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `ssu-align -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run ssu-align with typical input and output options.
