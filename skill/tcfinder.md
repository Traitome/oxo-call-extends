---
name: tcfinder
category: population-genomics
description: A lightweight tool to find clusters of samples within a phylogeny.
tags: [tcfinder, population-genomics, sam]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/tcfinder"
---

## Concepts

- **Tool Overview**: tcfinder (v1.0.0) - A lightweight tool to find clusters of samples within a phylogeny.
- **Core Function**: A lightweight tool to find clusters of samples within a phylogeny.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tcfinder`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tcfinder -i <input.vcf> -o <output_dir>`
**Explanation:** Run tcfinder with typical input and output options.
