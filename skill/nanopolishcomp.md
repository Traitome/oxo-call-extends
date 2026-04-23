---
name: nanopolishcomp
category: utility
description: NanopolishComp is a Python3 package for downstream analyses of Nanopolish output files
tags: [nanopolishcomp, utility, nanopolish, downstream, analysis]
author: oxo-call-community
source_url: "https://github.com/a-slide/NanopolishComp"
---

## Concepts

- **Tool Overview**: NanopolishComp v0.6.12 - downstream analysis of Nanopolish output files.
- **Core Function**: Processes and analyzes Nanopolish output for methylation and variant calling results.
- **Input/Output**: Takes Nanopolish output files; outputs processed analysis results.
- **Installation**: `conda install -c bioconda nanopolishcomp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Nanopolish output format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i nanopolish_output.tsv -o processed_results.tsv`
**Explanation:** Processes Nanopolish output for downstream analysis.
