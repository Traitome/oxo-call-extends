---
name: stellar
category: alignment
description: STELLAR is a tool for finding pairwise local alignments between long genomic or very many short sequences.
tags: [stellar, alignment]
author: oxo-call-community
source_url: "https://github.com/seqan/seqan/tree/master/apps/stellar/README"
---

## Concepts

- **Tool Overview**: stellar (v1.4.9) - STELLAR is a tool for finding pairwise local alignments between long genomic or very many short sequences.
- **Core Function**: STELLAR is a tool for finding pairwise local alignments between long genomic or very many short sequences.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stellar`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stellar -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run stellar with typical input and output options.
