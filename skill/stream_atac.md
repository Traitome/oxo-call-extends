---
name: stream_atac
category: alignment
description: STREAM-Single-cell Trajectories Reconstruction, Exploration And Mapping of single-cell data. Preprocessing steps for single cell atac-seq data.
tags: [stream_atac, alignment]
author: oxo-call-community
source_url: "https://github.com/pinellolab/STREAM_atac"
---

## Concepts

- **Tool Overview**: stream_atac (v0.3.5) - STREAM-Single-cell Trajectories Reconstruction, Exploration And Mapping of single-cell data. Preprocessing steps for single cell atac-seq data.
- **Core Function**: STREAM-Single-cell Trajectories Reconstruction, Exploration And Mapping of single-cell data. Preprocessing steps for single cell atac-seq data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stream_atac`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stream_atac -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run stream_atac with typical input and output options.
