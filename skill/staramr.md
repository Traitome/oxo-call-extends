---
name: staramr
category: assembly
description: Scan genome contigs against the ResFinder and PointFinder databases
tags: [staramr, assembly]
author: oxo-call-community
source_url: "https://github.com/phac-nml/staramr"
---

## Concepts

- **Tool Overview**: staramr (v0.12.1) - Scan genome contigs against the ResFinder and PointFinder databases
- **Core Function**: Scan genome contigs against the ResFinder and PointFinder databases
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda staramr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `staramr -i <reads.fastq> -o <output_dir>`
**Explanation:** Run staramr with typical input and output options.
