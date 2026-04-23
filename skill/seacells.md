---
name: seacells
category: expression
description: SEACells algorithm for Inference of transcriptional and epigenomic cellular states from single-cell genomics data.
tags: [seacells, expression]
author: oxo-call-community
source_url: "https://github.com/dpeerlab/SEACells"
---

## Concepts

- **Tool Overview**: seacells (v0.3.3) - SEACells algorithm for Inference of transcriptional and epigenomic cellular states from single-cell genomics data.
- **Core Function**: SEACells algorithm for Inference of transcriptional and epigenomic cellular states from single-cell genomics data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seacells`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seacells -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run seacells with typical input and output options.
