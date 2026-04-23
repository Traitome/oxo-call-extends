---
name: spapros
category: expression
description: Probe set selection for targeted spatial transcriptomics.
tags: [spapros, expression]
author: oxo-call-community
source_url: "https://spapros.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: spapros (v0.1.6) - Probe set selection for targeted spatial transcriptomics.
- **Core Function**: Probe set selection for targeted spatial transcriptomics.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda spapros`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `spapros -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run spapros with typical input and output options.
