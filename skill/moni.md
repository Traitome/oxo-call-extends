---
name: moni
category: alignment
description: A Pangenomics Index for Finding MEMs
tags: [moni, alignment, alignment]
author: oxo-call-community
source_url: "https://github.com/maxrossi91/moni"
---

## Concepts

- **Tool Overview**: moni v0.2.2 - MONI (Multi) is a Pangenomics Index for Finding Maximal Exact Matches (MEMs). It uses the prefix-free parsing of the text to build the Burrows-Wheeler Transform (BWT) of the reference genomes, the suffix array (SA) samples at the beginning and at the end of each run of the BWT, and the threshold positions..
- **Core Function**: A Pangenomics Index for Finding MEMs
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda moni`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
