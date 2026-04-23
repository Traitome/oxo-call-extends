---
name: skmer
category: alignment
description: Assembly-free and alignment-free tool for estimating genomic distances between genome-skims
tags: [skmer, alignment]
author: oxo-call-community
source_url: "https://github.com/shahab-sarmashghi/Skmer"
---

## Concepts

- **Tool Overview**: skmer (v3.3.0) - Assembly-free and alignment-free tool for estimating genomic distances between genome-skims
- **Core Function**: Assembly-free and alignment-free tool for estimating genomic distances between genome-skims
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda skmer`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `skmer -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run skmer with typical input and output options.
