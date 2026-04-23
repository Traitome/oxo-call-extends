---
name: cstag-cli
category: alignment
description: Command line interface of cstag to manipulate the minimap2's CS tag
tags: [cstag-cli, alignment]
author: oxo-call-community
source_url: "https://github.com/akikuno/cstag-cli"
---

## Concepts

- **Tool Overview**: cstag-cli (v1.0.0) - Command line interface of cstag to manipulate the minimap2's CS tag
- **Core Function**: Command line interface of cstag to manipulate the minimap2's CS tag
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda cstag-cli`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
