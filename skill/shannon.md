---
name: shannon
category: expression
description: A program for assembling transcripts from RNA-Seq data.
tags: [shannon, expression]
author: oxo-call-community
source_url: "http://sreeramkannan.github.io/Shannon/"
---

## Concepts

- **Tool Overview**: shannon (v0.0.2) - A program for assembling transcripts from RNA-Seq data.
- **Core Function**: A program for assembling transcripts from RNA-Seq data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shannon`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shannon -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run shannon with typical input and output options.
