---
name: unifrac
category: metagenomics
description: Fast phylogenetic diversity calculations.
tags: [unifrac, metagenomics]
author: oxo-call-community
source_url: "https://github.com/biocore/unifrac/blob/1.5.1/README.md"
---

## Concepts

- **Tool Overview**: unifrac (v1.5.1) - UniFrac is a commonly phylogenetic diversity distance metric used in microbiome research. The metric relates two microbiome samples together within the context of an evolutionary history, and produces a distance that corresponds to how similar two samples by the amount of overlapping branch length.
- **Core Function**: Fast phylogenetic diversity calculations.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda unifrac`

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
