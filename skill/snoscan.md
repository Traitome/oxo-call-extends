---
name: snoscan
category: epigenomics
description: Search for C/D box methylation guide snoRNA genes in a genomic sequence
tags: [snoscan, epigenomics]
author: oxo-call-community
source_url: "http://cryptogenomicon.org/snoscan-and-squid-in-the-21st-century.html"
---

## Concepts

- **Tool Overview**: snoscan (v1.0) - Search for C/D box methylation guide snoRNA genes in a genomic sequence
- **Core Function**: Search for C/D box methylation guide snoRNA genes in a genomic sequence
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snoscan`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snoscan -i <input.bam> -o <output_dir>`
**Explanation:** Run snoscan with typical input and output options.
