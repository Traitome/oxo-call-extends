---
name: taxmapper
category: alignment
description: Analysis pipeline for metagenomic, microeukaryotic sequencing data.
tags: [taxmapper, alignment]
author: oxo-call-community
source_url: "https://bitbucket.org/dbeisser/taxmapper"
---

## Concepts

- **Tool Overview**: taxmapper (v1.0.2) - Analysis pipeline for metagenomic, microeukaryotic sequencing data.
- **Core Function**: Analysis pipeline for metagenomic, microeukaryotic sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxmapper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxmapper -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run taxmapper with typical input and output options.
