---
name: unifrac-binaries
category: metagenomics
description: Fast phylogenetic diversity calculations
tags: [unifrac-binaries, metagenomics]
author: oxo-call-community
source_url: "https://github.com/biocore/unifrac-binaries"
---

## Concepts

- **Tool Overview**: unifrac-binaries (v1.6) - UniFrac is a commonly phylogenetic diversity distance metric used in microbiome research. The metric relates two microbiome samples together within the context of an evolutionary history, and produces a distance that corresponds to how similar two samples by the amount of overlapping branch length. This package contains command line utilities and a shared library.
- **Core Function**: Fast phylogenetic diversity calculations
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda unifrac-binaries`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
