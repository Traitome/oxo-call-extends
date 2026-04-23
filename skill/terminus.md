---
name: terminus
category: expression
description: Terminus enables the discovery of data-driven, robust transcript groups from RNA-seq data
tags: [terminus, expression]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/terminus"
---

## Concepts

- **Tool Overview**: terminus (v0.1.0) - Terminus enables the discovery of data-driven, robust transcript groups from RNA-seq data
- **Core Function**: Terminus enables the discovery of data-driven, robust transcript groups from RNA-seq data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda terminus`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `terminus -i <input.bam> -g <annotation.gtf> -o <output.tsv>`
**Explanation:** Run terminus with typical input and output options.
