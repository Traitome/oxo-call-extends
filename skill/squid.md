---
name: squid
category: expression
description: Detector for fusion-gene and non-fusion-gene transcriptomic structural variations from RNA-seq data.
tags: [squid, expression]
author: oxo-call-community
source_url: "https://github.com/Kingsford-Group/squid"
---

## Concepts

- **Tool Overview**: squid (v1.5) - Detector for fusion-gene and non-fusion-gene transcriptomic structural variations from RNA-seq data.
- **Core Function**: Detector for fusion-gene and non-fusion-gene transcriptomic structural variations from RNA-seq data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda squid`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `squid -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run squid with typical input and output options.
