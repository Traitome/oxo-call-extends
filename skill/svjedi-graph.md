---
name: svjedi-graph
category: variant-calling
description: SVJedi-graph is a structural variation (SV) genotyper for long read data using a variation graph to represent SVs.
tags: [svjedi-graph, variant-calling]
author: oxo-call-community
source_url: "https://github.com/SandraLouise/SVJedi-graph"
---

## Concepts

- **Tool Overview**: svjedi-graph (v1.2.1) - SVJedi-graph is a structural variation (SV) genotyper for long read data using a variation graph to represent SVs.
- **Core Function**: SVJedi-graph is a structural variation (SV) genotyper for long read data using a variation graph to represent SVs.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda svjedi-graph`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `svjedi-graph -i <input.bam> -r <reference.fasta> -o <output.vcf>`
**Explanation:** Run svjedi-graph with typical input and output options.
