---
name: seqan_tcoffee
category: alignment
description: SeqAn::T-Coffee - Multiple Sequence Alignment.
tags: [seqan_tcoffee, alignment]
author: oxo-call-community
source_url: "http://www.seqan.de/apps/seqan-t-coffee"
---

## Concepts

- **Tool Overview**: seqan_tcoffee (v1.13.8) - SeqAn::T-Coffee - Multiple Sequence Alignment.
- **Core Function**: SeqAn::T-Coffee - Multiple Sequence Alignment.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqan_tcoffee`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqan_tcoffee -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run seqan_tcoffee with typical input and output options.
