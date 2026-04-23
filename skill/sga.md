---
name: sga
category: formatting
description: SGA - String Graph Assembler. SGA is a de novo assembler for DNA sequence reads. It is based on Gene Myers string graph formulation of assembly and uses the FM-index/Burrows-Wheeler transform to efficiently find overlaps between sequence reads.
tags: [sga, formatting]
author: oxo-call-community
source_url: "https://github.com/jts/sga"
---

## Concepts

- **Tool Overview**: sga (v0.10.15) - SGA - String Graph Assembler. SGA is a de novo assembler for DNA sequence reads. It is based on Gene Myers string graph formulation of assembly and uses the FM-index/Burrows-Wheeler transform to efficiently find overlaps between sequence reads.
- **Core Function**: SGA - String Graph Assembler. SGA is a de novo assembler for DNA sequence reads. It is based on Gene Myers string graph formulation of assembly and uses the FM-index/Burrows-Wheeler transform to efficiently find overlaps between sequence reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sga`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sga -i <input_file> -o <output_file>`
**Explanation:** Run sga with typical input and output options.
