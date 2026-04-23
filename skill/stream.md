---
name: stream
category: alignment
description: STREAM-Single-cell Trajectories Reconstruction, Exploration And Mapping
tags: [stream, alignment]
author: oxo-call-community
source_url: "https://github.com/pinellolab/STREAM"
---

## Concepts

- **Tool Overview**: stream (v1.1) - STREAM-Single-cell Trajectories Reconstruction, Exploration And Mapping
- **Core Function**: STREAM-Single-cell Trajectories Reconstruction, Exploration And Mapping
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stream`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stream -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run stream with typical input and output options.
