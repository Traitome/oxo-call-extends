---
name: seqsero2
category: alignment
description: Salmonella serotype prediction from genome sequencing data.
tags: [seqsero2, alignment]
author: oxo-call-community
source_url: "https://github.com/denglab/SeqSero2"
---

## Concepts

- **Tool Overview**: seqsero2 (v1.3.2) - Salmonella serotype prediction from genome sequencing data.
- **Core Function**: Salmonella serotype prediction from genome sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqsero2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqsero2 -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run seqsero2 with typical input and output options.
