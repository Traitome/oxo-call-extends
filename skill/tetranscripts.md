---
name: tetranscripts
category: expression
description: A package for including transposable elements in differential enrichment analysis of sequencing datasets.
tags: [tetranscripts, expression]
author: oxo-call-community
source_url: "http://hammelllab.labsites.cshl.edu/software#TEToolkit"
---

## Concepts

- **Tool Overview**: tetranscripts (v2.2.3) - A package for including transposable elements in differential enrichment analysis of sequencing datasets.
- **Core Function**: A package for including transposable elements in differential enrichment analysis of sequencing datasets.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tetranscripts`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tetranscripts -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run tetranscripts with typical input and output options.
