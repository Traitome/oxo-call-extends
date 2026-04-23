---
name: srnamapper
category: alignment
description: Mapping small RNA data to a genome.
tags: [srnamapper, alignment]
author: oxo-call-community
source_url: "https://github.com/mzytnicki/srnaMapper"
---

## Concepts

- **Tool Overview**: srnamapper (v1.0.12) - Mapping small RNA data to a genome.
- **Core Function**: Mapping small RNA data to a genome.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda srnamapper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `srnamapper -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run srnamapper with typical input and output options.
