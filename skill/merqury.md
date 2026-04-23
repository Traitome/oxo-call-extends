---
name: merqury
category: assembly
description: Evaluate genome assemblies with k-mers and more.
tags: [merqury, assembly]
author: oxo-call-community
source_url: "https://github.com/marbl/merqury"
---

## Concepts

- **Tool Overview**: merqury v1.3 - Often, genome assembly projects have illumina whole genome sequencing reads available for the assembled individual. The k-mer spectrum of this read set can be used for independently evaluating assembly quality without the need of a high quality reference. Merqury provides a set of tools for this purpose..
- **Core Function**: Evaluate genome assemblies with k-mers and more.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda merqury`

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
