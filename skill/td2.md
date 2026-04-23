---
name: td2
category: expression
description: TD2: a tool to find protein coding regions in transcripts.
tags: [td2, expression]
author: oxo-call-community
source_url: "https://github.com/Markusjsommer/TD2"
---

## Concepts

- **Tool Overview**: td2 (v1.0.8) - TD2: a tool to find protein coding regions in transcripts.
- **Core Function**: TD2: a tool to find protein coding regions in transcripts.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda td2`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `td2 -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run td2 with typical input and output options.
