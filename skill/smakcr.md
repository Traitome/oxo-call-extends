---
name: smakcr
category: expression
description: Count short k-mers fast
tags: [smakcr, expression]
author: oxo-call-community
source_url: "https://github.com/julibeg/smakcr"
---

## Concepts

- **Tool Overview**: smakcr (v0.1.0) - Count short k-mers fast
- **Core Function**: Count short k-mers fast
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smakcr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smakcr -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run smakcr with typical input and output options.
