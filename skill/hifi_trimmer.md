---
name: hifi_trimmer
category: qc
description: hifi-trimmer is a tool for filtering and trimming extraneous adapter hits from a HiFi read set using a BLAST search.
tags: [hifi_trimmer, qc]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/hifi-trimmer"
---

## Concepts

- **Tool Overview**: hifi_trimmer (v3.1.0) - hifi-trimmer is a tool for filtering and trimming extraneous adapter hits from a HiFi read set using a BLAST search.
- **Core Function**: Provides functionality for qc tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda hifi_trimmer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
